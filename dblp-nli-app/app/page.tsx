"use client";
import { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Textarea } from "@/components/ui/textarea";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import {toast, Toaster} from "sonner";
import { Loader2 } from "lucide-react";

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
  const [queryResult, setQueryResult] = useState<SPARQLResult | null>(null);
  const [loading, setLoading] = useState(false);
  const [running, setRunning] = useState(false);

  const exampleQuestions = [
    "Who are the authors of 'NFDI4DS Gateway and Portal'?",
    "In which institutions does Ricardo Usbeck work?",
    "Question Answering papers published in ISWC."
  ];

  const handleExampleClick = (question: string) => {
    setUserQuery(question);
  };

  const handleGenerateSPARQL = async () => {
    if (!userQuery.trim()) {
      toast.error("Query input cannot be empty.");
      return;
    }
    setLoading(true);
    try {
      await new Promise((resolve) => setTimeout(resolve, 1000));
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
    } catch (error) {
      console.error("SPARQL generation error:", error);
      toast.error("Error generating SPARQL.");
    } finally {
        setLoading(false)
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
            onChange={(e) => setUserQuery(e.target.value)}
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

            <Button onClick={handleRunSPARQL} disabled={running}>
              {running ? (
                <><Loader2 className="mr-2 h-4 w-4 animate-spin" /> Running...</>
              ) : (
                "Run Query"
              )}
            </Button>
          {running && <p className="text-sm text-gray-500">Running SPARQL query...</p>}
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
