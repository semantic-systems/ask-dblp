"use client";
import {useEffect, useState} from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Textarea } from "@/components/ui/textarea";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import {toast, Toaster} from "sonner";
import { Loader2 } from "lucide-react";
import {MdOutlineThumbDown, MdOutlineThumbUp} from 'react-icons/md';
import Image from "next/image";
import CodeMirror from "@uiw/react-codemirror";
import { StreamLanguage } from "@codemirror/language";
import { sparql } from "@codemirror/legacy-modes/mode/sparql";
import { EditorView } from "@codemirror/view";

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

type LinkedEntity = {
  original_label: string;
  normalized_label: string;
  uri: string;
};

type EntityGroup = {
  entity_type: string;
  entities: LinkedEntity[];
};

type GroupedEntityUI = {
  entity_type: string;
  options: LinkedEntity[];
  selected: LinkedEntity;
};

type EntityWithType = LinkedEntity & {
  entity_type: string;
};

export default function SPARQLQueryApp() {
  const [userQuery, setUserQuery] = useState("");
  const [sparqlQuery, setSparqlQuery] = useState("");
  const [queryDescription, setQueryDescription] = useState("");
  const [queryResult, setQueryResult] = useState<SPARQLResult | null>(null);
  const [loading, setLoading] = useState(false);
  const [running, setRunning] = useState(false);
  const [entityLinkingGroups, setEntityLinkingGroups] = useState<GroupedEntityUI[]>([]);
  const [prevUsedEntities, setPrevUsedEntities] = useState<EntityWithType[]>([]);

  const exampleQuestions = [
    "Top 10 most frequent authors who have published at the International Semantic Web Conference (ISWC).",
    "Database papers published in the Semantic Web Journal.",
    "Who are the highly cited coauthors of Hannah Bast?"
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
      } catch (error: unknown) {
        // toast.error(`Error validating question. (${error?.message || error})`);
        // return { valid: false, feedback: "Network or server error occurred." };
        let message = "Error validating question.";
        if (error instanceof Error) {
            message += ` (${error.message})`;
        } else if (typeof error === "string") {
            message += ` (${error})`;
        }
        toast.error(message);
        return { valid: false, feedback: "Network or server error occurred." };
      }
  };

  const updateSparqlQuery = (txt: string) => {
    setSparqlQuery(txt);
  };

  const extractQueryDescription = (txt: string): string | undefined => {
    const m = txt.match(/#\s*ASK-DBLP: (.+?)\n/);

    if (m) {
      return m[1];
    }
  };

  const replaceQueryDescription = (query: string, newDescription: string): string => {
    const newDescriptionLine = `# ASK-DBLP: ${newDescription}\n`;
    return query.replace(/#\s*ASK-DBLP: (.+?)\n/, newDescriptionLine);
  };

  useEffect(() => {
    const newQueryDescription = extractQueryDescription(sparqlQuery);
    setQueryDescription(newQueryDescription || "");
  }, [sparqlQuery]);

  const updateQueryDescription = (newQueryDescription: string) => {
    const newQuery = replaceQueryDescription(sparqlQuery, newQueryDescription);
    setSparqlQuery(newQuery);
    setQueryDescription(newQueryDescription);
  };

  const handleExampleClick = async (question: string) => {
    setUserQuery(question);
    setSparqlQuery("");
    setQueryResult(null);
    setEntityLinkingGroups([]);
    //await handleGenerateSPARQL(question);
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
      const validation = await validateQuestion(query);
      if (!validation.valid) {
        toast.warning(validation.feedback || "Invalid question.");
        // return;
      }
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
      const ask_dblp_string = `# ASK-DBLP: ${userQuery}`;
      updateSparqlQuery(`${confidence_string}\n${ask_dblp_string} \n${data.sparql}`);
      const allEntities: EntityGroup[] = data.linked_entities || [];
      const entitiesInSparql = data.entities_used_in_sparql || [];

      setPrevUsedEntities(entitiesInSparql);
      const groupedEntities = allEntities.map((group: EntityGroup): GroupedEntityUI => {
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
    const selectedEntities: EntityWithType[] = entityLinkingGroups.map(group => ({
      entity_type: group.entity_type,
      normalized_label: group.selected?.normalized_label || "",
      original_label: group.selected?.original_label || "",
      uri: group.selected?.uri || "",
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
      <header className="flex items-center space-x-4 p-4 border-b">
        <Image
          src="/ask-dblp-logo.png"
          alt="ASK DBLP Logo"
          width={300}
          height={100}
          priority
        />
      </header>
      <Card className="mb-4">
        <CardContent className="p-4 space-y-2">
          <p className="text-justify text-sm text-gray-600 font-bold">
            Welcome to ASK-DBLP! <br/> <br/>
            ASK-DBLP offers a natural language interface (NLI) that allows users to question the DBLP Knowledge Graph.
            The system generates a corresponding SPARQL query, which you can review and edit. Once ready, it executes the query against the DBLP SPARQL endpoint and displays the results. <br/>
          </p>
          <p className="text-sm text-gray-600 font-bold">

          </p>
          <Input
            placeholder="Type your question or select from the sample questions below."
            value={userQuery}
            onChange={(e) => {
              setUserQuery(e.target.value);
              setSparqlQuery("");
              setQueryResult(null);
              setEntityLinkingGroups([]);
            }}
          />
          <div className="overflow-x-auto flex flex-col items-start gap-2 mt-2 py-2 px-1">
            {exampleQuestions.map((question, index) => (
              <Button
                key={index}
                variant="outline"
                className="text-left w-auto"
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
                      const selected = group.options.find(opt => opt.uri === selectedUri)!;
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
            <CodeMirror
              value={sparqlQuery}
              height="300px"
              basicSetup={{
                lineNumbers: true,
                highlightActiveLineGutter: true,
                highlightActiveLine: true,
              }}
              extensions={[
                StreamLanguage.define(sparql),
                EditorView.lineWrapping,
              ]}
              onChange={(value) => updateSparqlQuery(value)}
              theme="light"
            />

            <div className="row flex">
              <span className="block text-gray-700 text-sm font-bold mt-2 mb-2 mr-2">
                Description
              </span>
              <Input placeholder="Describe your query" value={queryDescription}
                     onChange={(e) => updateQueryDescription(e.target.value)}/>
            </div>

            <div className="row flex">
              <div className="flex">
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
                    <tr key={rowIndex} className="border-t">
                      <td className="p-2 text-sm text-gray-600 font-mono">{rowIndex + 1}.</td>
                      {queryResult.head.vars.map((varName, colIndex) => {
                        const valueObj = binding[varName];
                        const value = valueObj?.value || "";
                        const isUri = valueObj?.type === "uri";

                        return (
                          <td key={colIndex} className="p-2 text-sm text-gray-800">
                            {isUri ? (
                              <a href={value} target="_blank" rel="noopener noreferrer" className="text-blue-600 underline">
                                {value}
                              </a>
                            ) : (
                              value
                            )}
                          </td>
                        );
                      })}
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