"use client";
import { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Textarea } from "@/components/ui/textarea";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import {toast, Toaster} from "sonner";
import { Loader2 } from "lucide-react";
import {MdOutlineThumbDown, MdOutlineThumbUp} from 'react-icons/md';

interface SPARQLResult {
  head: {
    vars: string[];
  };
  results: {
    bindings: {
      [key: string]: {
        type: string;
        value: string;
      };
    }[];
  };
}

export default function SPARQLQueryApp() {
  const [userQuery, setUserQuery] = useState("");
  const [sparqlQuery, setSparqlQuery] = useState("");
  const [queryResult, setQueryResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [running, setRunning] = useState(false);
  const [entityLinkingGroups, setEntityLinkingGroups] = useState([]);
  const [prevUsedEntities, setPrevUsedEntities] = useState([]);

  const exampleQuestions = [
    "Who were the co-authors of Ashish Vaswani in the paper ‘Attention is all you need’?",
    "Who are the highly cited coauthors of Hannah Bast?",
    "Database papers published in ISWC."
  ];
  const validateQuestion = async (question: string): Promise<{ valid: boolean; feedback?: string }> => {
      try {
        const checker_result = await fetch('/api/question_checker', {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ query: question }),
        });

        if (!checker_result.ok) {
          toast.error(`Error checking question. (HTTP ${checker_result.status})`);
          return { valid: false, feedback: "API returned an error response." };
        }

        const checker_result_response = await checker_result.json();
        const completeness = checker_result_response.completeness;

        // optional delay for user feedback
        await new Promise((res) => setTimeout(res, 300));

        if (completeness) {
          return { valid: true };
        } else {
          return {
            valid: false,
            feedback: checker_result_response.feedback ?? "Invalid Question!",
          };
        }
      } catch (err: any) {
        toast.error(`Error validating question. (${err.message || err})`);
        return { valid: false, feedback: "Network or server error occurred." };
      }
  };

  const handleExampleClick = async (question: string) => {
    setUserQuery(question);
    setSparqlQuery("");
    setQueryResult(null);
    setEntityLinkingGroups([]);
    await handleGenerateSPARQL(question);
  };

  const handleGenerateSPARQL = async (exampleQuery?: string) => {
    const query = exampleQuery || userQuery;
    if (!query.trim()) {
      toast.error("Query input cannot be empty.");
      return;
    }
    setLoading(true);
    setSparqlQuery("");
    setQueryResult(null);
    setEntityLinkingGroups([]);
    try {
      await new Promise((resolve) => setTimeout(resolve, 1000));
//       const validation = await validateQuestion(query);
//       if (!validation.valid) {
//         toast.warning(validation.feedback || "Invalid question.");
//         return;
//       }
      const response = await fetch('/api/generate_sparql', {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query: userQuery }),
      });
      const data = await response.json();
      if (response.status >= 400) {
        toast.error(`Error generating SPARQL. (${data.error})`);
        return;
      }
      const confidence_string = `# Confidence_score: ${data.confidence_score}`;
      setSparqlQuery(`${confidence_string}\n ${data.sparql}`);
      const allEntities = data.linked_entities || [];
      const entitiesInSparql = data.entities_used_in_sparql || [];

      setPrevUsedEntities(entitiesInSparql);
      const groupedEntities = allEntities.map((group) => {
        const options = group.entities.map(entity => ({
           original_label: entity.original_label,
           normalized_label: entity.normalized_label,
           uri: entity.uri
         }));

        return {
         entity_type: group.entity_type || "Unknown",
         options,
         selected: options[0]  // default selected entity
        };
      });

      setEntityLinkingGroups(groupedEntities);
      toast.message("SPARQL generated. You may select another entity below.");
    } catch (error) {

      console.error("SPARQL generation error:", error);
      toast.error("Error generating SPARQL.");
    } finally {
        setLoading(false)
    }
  };

  const handleRegenerate = async () => {
    if (!sparqlQuery || !userQuery) {
      toast.error("Missing original SPARQL or question.");
      return;
    }
    const selectedEntities = entityLinkingGroups.map(group => ({
      entity_type: group.entity_type,
      normalized_label: group.selected?.normalized_label ?? group.selected?.label,
      original_label: group.selected?.original_label ?? group.selected?.label,
      uri: group.selected?.uri,
    }));

    if (selectedEntities.some(entity => !entity.uri)) {
      toast.warning("Please select an entity in each group before regenerating.");
      return;
    }

    const hasChanged = JSON.stringify(selectedEntities) !== JSON.stringify(prevUsedEntities);

    if (!hasChanged) {
      toast.info("Selected entities are the same as before. No regeneration needed.");
      return;
    }

    try {
      setLoading(true);

      const response = await fetch("/api/regenerate_sparql", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          question: userQuery,
          previous_entities: prevUsedEntities,
          selected_entities: selectedEntities,
          sparql: sparqlQuery
        })
      });

      if (!response.ok) {
        throw new Error("Regeneration request failed");
      }

      const data = await response.json();

      if (data.sparql) {
        setSparqlQuery(data.sparql);
        setPrevUsedEntities(selectedEntities);
        toast.success("SPARQL regenerated with new entity selections.");
      } else {
        toast.error("Regeneration returned no SPARQL.");
      }

    } catch (error) {
      console.error("Regeneration error:", error);
      toast.error("Failed to regenerate SPARQL.");
    } finally {
      setLoading(false);
    }
  };

  const handleRunSPARQL = async () => {
    if (!sparqlQuery.trim()) {
      toast.error("Query input cannot be empty.");
      return;
    }
    setRunning(true);
    try {
      await new Promise((resolve) => setTimeout(resolve, 1000));
      const response = await fetch('/api/run_sparql', {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user_query: userQuery, query: sparqlQuery }),
      });
      const data = await response.json();
      setQueryResult(data.sparql_results);
    } catch (error) {
      console.error("Failed to run SPARQL query:", error);
      toast.error("Failed to run SPARQL query.");
    } finally {
        setRunning(false);
    }
  };

  const rankUp = () => {
    toast.info('The query has been marked as sufficient');
  };

  const rankDown = () => {
    toast.info('The query has been marked as not sufficient');
  };

  return (
    //<div className="max-w-2xl mx-auto p-6 space-y-4">
    <div className="max-w-6xl mx-auto overflow-x-auto">
      <Card className="mb-4">
        <CardContent className="p-4 space-y-2">
          <p className="text-justify text-sm text-gray-600">
            Welcome to ASK-DBLP! <br/> <br/>
            ASK-DBLP offers a natural language interface (NLI) that allows users to question the DBLP Knowledge Graph.
            The system generates a corresponding SPARQL query, which you can review and edit. Once ready, it executes the query against the DBLP SPARQL endpoint and displays the results. <br/>

          </p>
          <p className="text-sm text-gray-600">
             Type your question or choose from the sample questions below.
          </p>
          <Input
            placeholder="Enter your query"
            value={userQuery}
            onChange={(e) => {
              setUserQuery(e.target.value);
              setSparqlQuery("");
              setQueryResult(null);
              setEntityLinkingGroups([]);
            }}
          />
          <div className="flex flex-wrap gap-2">
            {exampleQuestions.map((question, index) => (
              <Button
                key={index}
                variant="outline"
                onClick={() => handleExampleClick(question)}
              >
                {question}
              </Button>
            ))}
          </div>
          <Button onClick={() => handleGenerateSPARQL()} disabled={loading}>
            {loading ? (
              <><Loader2 className="mr-2 h-4 w-4 animate-spin" /> Generating...</>
            ) : (
              "Generate SPARQL"
            )}
          </Button>
          {loading && <p className="text-sm text-gray-500">Generating SPARQL query...</p>}

          {entityLinkingGroups.length > 0 && (
            <div className="space-y-4">
              {prevUsedEntities.length > 0 && (
                 <div>
                   <p className="text-sm font-semibold">Entities used in SPARQL:</p>
                   <ul className="list-disc pl-5">
                      {prevUsedEntities.map((entity, idx) => (
                        <li key={idx}>
                          [{entity.entity_type}] {entity.original_label} → {entity.uri}
                        </li>
                      ))}
                   </ul>
                 </div>
               )}
              <p className="text-sm font-semibold">Linked Entities (select to refine):</p>
              {entityLinkingGroups.map((group, groupIndex) => (
                <div key={groupIndex}>
                  <label className="text-sm font-medium">{group.entity_type}</label>
                  <select
                    className="w-full border rounded p-2 mt-1"
                    value={group.selected?.uri}
                    onChange={(e) => {
                      const selectedUri = e.target.value;
                      const selected = group.options.find(opt => opt.uri === selectedUri);
                      const updatedGroups = [...entityLinkingGroups];
                      updatedGroups[groupIndex].selected = selected;
                      setEntityLinkingGroups(updatedGroups);
                    }}
                  >
                    {group.options.map((entity, idx) => (
                      <option key={idx} value={entity.uri}>{entity.original_label}</option>
                    ))}
                  </select>
                </div>
              ))}
              <Button className="mt-2" onClick={handleRegenerate}>Update SPARQL with Selected Entities</Button>
            </div>
          )}
        </CardContent>
      </Card>

      {sparqlQuery && (
        <Card className="mb-4">
          <CardContent className="p-4 space-y-2">
            <Textarea
              className="w-full"
              rows={10}
              value={sparqlQuery}
              onChange={(e) => setSparqlQuery(e.target.value)}
            />

            <div className="row flex">
              <div className="row flex">
                <button
                  className="rounded-md rounded-r-none bg-gray-600 py-2 px-4 border border-transparent text-center text-sm text-white hover:cursor-pointer transition-all shadow-md hover:shadow-lg focus:shadow-none active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
                  title="Generated query is not sufficient"
                  type="button"
                  onClick={rankDown}
                >
                  <MdOutlineThumbDown/>
                </button>
                <button
                  className="rounded-md rounded-l-none bg-black py-2 px-4 border border-transparent text-center text-sm text-white hover:cursor-pointer transition-all shadow-md hover:shadow-lg focus:shadow-none active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
                  title="Generated query is sufficient"
                  type="button"
                  onClick={rankUp}
                >
                  <MdOutlineThumbUp/>
                </button>
              </div>
              <div className="ml-3">
                <Button onClick={handleRunSPARQL} disabled={running}>
                  {running ? (
                    <><Loader2 className="mr-2 h-4 w-4 animate-spin" /> Running...</>
                  ) : (
                    "Run Query"
                  )}
                </Button>
                {running && <span className="text-sm text-gray-500 ml-2">Running SPARQL query...</span>}
              </div>
            </div>
          </CardContent>
        </Card>
      )}
      {queryResult && queryResult.results?.bindings?.length > 0 && (
          <Card className="mb-4">
            <CardContent className="p-4 overflow-x-auto">
              <h2 className="font-bold text-lg mb-2">Results:</h2>
              <table className="w-full table-auto border-collapse border border-gray-300">
                <thead>
                  <tr>
                    <th className="border border-gray-300 px-4 py-2 text-left font-semibold bg-gray-100">No</th>
                    {queryResult.head.vars.map((varName, index) => (
                      <th key={index} className="border border-gray-300 px-4 py-2 text-left font-semibold bg-gray-100">
                        {varName}
                      </th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {queryResult.results.bindings.map((binding, rowIndex) => (
                    <tr key={rowIndex} className="hover:bg-gray-50">
                      <td className="border border-gray-300 px-4 py-2">{rowIndex + 1}</td>
                      {queryResult.head.vars.map((varName, colIndex) => (
                        <td key={colIndex} className="border border-gray-300 px-4 py-2">
                          {binding[varName]?.value || ""}
                        </td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            </CardContent>
          </Card>
        )}
        <Toaster/>
        </div>
      );
}