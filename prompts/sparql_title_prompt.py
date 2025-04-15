from langchain.prompts import PromptTemplate


prompt_template = """
You are a helpful data scientist that can summarize SPARQL queries.

Generate a brief 10-word-maximum title for the SPARQL query below.

===SPARQL Query
{query}

===Response Format
Please respond in below JSON format:
{{
    "title": "This is a title"
}}
"""

SPARQL_TITLE_PROMPT = PromptTemplate.from_template(prompt_template)