from SPARQLWrapper import SPARQLWrapper, JSON
from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os


parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ""))
sys.path.append(parent_dir)
import llms
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)  # Allow frontend to access backend


@app.route('/generate_sparql', methods=['POST'])
def generate_sparql():
   data = request.json
   user_query = data.get("query", "")
   sparql_query = llms.question_to_sparql(user_query)
   return jsonify({"sparql": sparql_query})


@app.route('/run_sparql', methods=['POST'])
def run_sparql():
   data = request.json
   sparql_query = data.get("query", "")
   print(sparql_query)
   SPARQL_ENDPOINT = app.config['SPARQL_ENDPOINT']
   try:
      sparql = SPARQLWrapper(SPARQL_ENDPOINT)
      sparql.setQuery(sparql_query)
      sparql.setReturnFormat(JSON)
      results = sparql.query().convert()
      print(results)
      return jsonify({"sparql_results": results})
   except Exception as e:
      return jsonify({"error": f"An exception occurred: {str(e)}"}), 500


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=9000, debug=True)