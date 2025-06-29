from langchain.prompts import PromptTemplate

prompt_template = """
You are the DBLP Knowledge Graph expert.

Please help to generate a SPARQL query to answer the question. Your response should ONLY be based on the given context and follow the response guidelines and format instructions.
Select the appropriate property URI while creating the SPARQL from the Knowledge Graph Schema.

===DBLP Knowledge Graph schema
{dblp_schema}

===Examples
{examples}

===Response Guidelines
1. If the provided context is sufficient, please generate a valid SPARQL query without any explanations for the question. The SPARQL should start with a comment containing the concatenation of ASK-DBLP: and the question being asked.
2. If the provided context is insufficient, please explain why it can't be generated.
3. Please use the most relevant relation(s).
4. Please format the query before responding.
5. Please always respond with a valid well-formed JSON object with the following format

===Response Format
{{
    "sparql": "A generated SPARQL query when context is sufficient."
}}

===Question
{question}

===Entities
{entities}
"""

QUESTION_TO_SPARQL_PROMPT = PromptTemplate.from_template(prompt_template)