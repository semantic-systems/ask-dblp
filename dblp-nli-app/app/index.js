import { useState } from 'react';

   export default function Home() {
     const [userQuery, setUserQuery] = useState('');
     const [sparqlQuery, setSparqlQuery] = useState('');
     const [results, setResults] = useState(null);

     const handleUserQueryChange = (e) => {
       setUserQuery(e.target.value);
     };

     const handleConvertToSPARQL = async () => {
       const response = await fetch('http://localhost:5000/api/convert', {
         method: 'POST',
         headers: {
           'Content-Type': 'application/json',
         },
         body: JSON.stringify({ query: userQuery }),
       });
       const data = await response.json();
       setSparqlQuery(data.sparql);
     };

     const handleSPARQLEdit = (e) => {
       setSparqlQuery(e.target.value);
     };

     const handleRunSPARQL = async () => {
       const response = await fetch('http://localhost:5000/api/run', {
         method: 'POST',
         headers: {
           'Content-Type': 'application/json',
         },
         body: JSON.stringify({ sparql: sparqlQuery }),
       });
       const data = await response.json();
       setResults(data.results);
     };

     return (
       <div>
         <h1>SPARQL Converter and Query App</h1>
         <div>
           <h2>User Query</h2>
           <textarea
             value={userQuery}
             onChange={handleUserQueryChange}
             placeholder="Enter your query here"
           ></textarea>
         </div>
         <button onClick={handleConvertToSPARQL}>Convert to SPARQL</button>
         <div>
           <h2>SPARQL Query</h2>
           <textarea
             value={sparqlQuery}
             onChange={handleSPARQLEdit}
             placeholder="SPARQL will appear here"
           ></textarea>
         </div>
         <button onClick={handleRunSPARQL}>Run SPARQL</button>
         <div>
           <h2>Results</h2>
           {results && results.map((result) => (
             <div key={result.id}>
               {result.name}
             </div>
           ))}
         </div>
       </div>
     );
   }