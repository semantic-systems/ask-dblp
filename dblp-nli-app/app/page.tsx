"use client";
import { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Textarea } from "@/components/ui/textarea";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import {toast, Toaster} from "sonner";

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

  const exampleQuestions = [
    "What are the papers Ricardo Usbeck published with Debayan Banerjee?",
    "Who are the authors of 'NFDI4DS Gateway and Portal.'?",
    "When was the first paper of Ricardo Usbeck Published?",
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
    try {
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

      setSparqlQuery(data.sparql);
    } catch (error) {
      console.error("SPARQL generation error:", error);
      toast.error("Error generating SPARQL.");
    }
  };

  const handleRunSPARQL = async () => {
    try {
      const response = await fetch('/api/run_sparql', {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query: sparqlQuery }),
      });
      const data = await response.json();
      setQueryResult(data.sparql_results);
    } catch (error) {
      console.error("Failed to run SPARQL query:", error);
      toast.error("Failed to run SPARQL query.");
    }
  };

  return (
    //<div className="max-w-2xl mx-auto p-6 space-y-4">
    <div className="max-w-6xl mx-auto overflow-x-auto">
      <Card className="mb-4">
        <CardContent className="p-4 space-y-2">
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
          <Button onClick={handleGenerateSPARQL}>Generate SPARQL</Button>
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
            <Button onClick={handleRunSPARQL}>Run Query</Button>
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
