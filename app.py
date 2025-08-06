import logging

from SPARQLWrapper import SPARQLWrapper, JSON
from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os
import json
import kgqa

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ""))
sys.path.append(parent_dir)
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)  # Allow frontend to access backend

CACHE_FILE = "sparql_cache.json"
query_cache = {}


def load_cache():
   global query_cache
   if os.path.exists(CACHE_FILE):
      with open(CACHE_FILE, "r", encoding="utf-8") as f:
         query_cache = json.load(f)


def save_cache():
   with open(CACHE_FILE, "w", encoding="utf-8") as f:
      json.dump(query_cache, f, ensure_ascii=False, indent=2)


@app.route('/question_checker',methods=['POST'])
def question_checker():
   try:
       data = request.json
       user_query = data.get("query", "")
       validation_result = kgqa.question_checker(user_query)
       completeness = validation_result['completeness']
       feedback = validation_result['feedback']
       if completeness =='complete':
           return jsonify({'completeness': True, 'feedback': feedback})
       else:
           return jsonify({'completeness': False, 'feedback': feedback})
   except Exception as e:
       return jsonify({"error": f"An exception occurred: {str(e)}"}), 500


@app.route('/entity_linking', methods=['POST'])
def entity_linking():
   try:
      data = request.json
      user_query = data.get("query", "")
      entities = kgqa.entity_linker(user_query)
      # print(entities)
      return jsonify({"linked_entities": entities})
   except Exception as e:
      return jsonify({"error": f"An exception occurred: {str(e)}"}), 500


@app.route('/generate_sparql', methods=['POST'])
def generate_sparql():
   # load_cache()
   try:
      data = request.json
      user_query = data.get("query", "")
      # entities = kgqa.entity_linker(user_query)
      sparql_query, confidence, linked_entities, selected_entities = kgqa.question_to_sparql(user_query)
      # query_cache[user_query] = {"sparql": sparql_query, "confidence_score": confidence}
      # save_cache()
      return jsonify({"sparql": sparql_query, "confidence_score": confidence,
                      "linked_entities": linked_entities, "entities_used_in_sparql": selected_entities})
   except Exception as e:
      # query_cache[user_query] = {"sparql": "", "confidence_score": 0}
      # save_cache()
      logging.error(str(e), exc_info=e)
      return jsonify({"error": f"An exception occurred: {str(e)}"}), 500


@app.route('/regenerate_sparql', methods=['POST'])
def regenerate_sparql():
    try:
        data = request.json
        question = data.get("question")
        original_sparql = data.get("sparql")
        previous_entities = data.get("previous_entities", [])
        selected_entities = data.get("selected_entities", [])
        # Replace old entities with new ones in the original SPARQL
        regenerated_sparql = original_sparql
        for old_entity, new_entity in zip(previous_entities, selected_entities):
            if old_entity["uri"] != new_entity["uri"]:
                regenerated_sparql = regenerated_sparql.replace(old_entity["uri"], new_entity["uri"])

        return jsonify({
            "sparql": regenerated_sparql,
            "message": "SPARQL regenerated with updated entities."
        })

    except Exception as e:
        return jsonify({"error": f"Error regenerating SPARQL: {str(e)}"}), 500


@app.route('/run_sparql', methods=['POST'])
def run_sparql():
   # load_cache()
   data = request.json
   user_query = data.get("user_query", "")
   sparql_query = data.get("query", "")
   # if user_query in query_cache:
   #    if query_cache[user_query].get("sparql","").strip() not in sparql_query.strip():
   #       query_cache[user_query].update({"user_updated_sparql":sparql_query})
         # save_cache()
   # print(sparql_query)
   SPARQL_ENDPOINT = app.config['SPARQL_ENDPOINT']
   try:
      sparql = SPARQLWrapper(SPARQL_ENDPOINT)
      sparql.setQuery(sparql_query)
      sparql.setReturnFormat(JSON)
      results = sparql.query().convert()
      #query_cache[user_query].update({"answer": utils.extruct_values(results)})
      # print(results)
      # save_cache()
      return jsonify({"sparql_results": results})
   except Exception as e:
      #query_cache[user_query].update({"answer": "No answer found!"})
      # save_cache()
      return jsonify({"error": f"An exception occurred: {str(e)}"}), 500



if __name__ == '__main__':
   app.run(host='0.0.0.0', port=9000, debug=True)