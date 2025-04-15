from langchain.prompts import PromptTemplate

prompt_template = """
You are the DBLP Knowledge Graph expert.

Please help to generate a SPARQL query to answer the question. Your response should ONLY be based on the given context and follow the response guidelines and format instructions.

===DBLP Knowledge Graph
{dblp_schemas}

===Example
{examples}

===Response Guidelines
1. If the provided context is sufficient, please generate a valid SPARQL query without any explanations for the question. The SPARQL should start with a comment containing the question being asked.
2. If the provided context is insufficient, please explain why it can't be generated.
3. Please use the most relevant relation(s).
5. Please format the query before responding.
6. Please always respond with a valid well-formed JSON object with the following format

===Response Format
{{
    "query": "A generated SPARQL query when context is sufficient.",
    "explanation": "An explanation of failing to generate the query."
}}

===Question
{question}
"""

QUESTION_TO_SPARQL_PROMPT = PromptTemplate.from_template(prompt_template)