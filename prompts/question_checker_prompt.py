from langchain.prompts import PromptTemplate
# A question may be incomplete if:
# - It includes only a first or last name without full author details.
# - It refers to something vague like "this paper", "he", or "it".
# - It lacks key information like the name of a paper, author, venue, or year.
# - It uses subjective terms like "best" without specifying a criterion (e.g., citations, awards).
# **Example 1**
#   Question: *What papers did John write?*
#   Response: *Your question is unclear — could you please specify the full name of the author? “John” is too ambiguous.*
#
# ---
#
# **Example 2**
#   Question: *What is the best KGQA paper?*
#   Response: *“Best” can mean different things (e.g., most cited, award-winning, or highest benchmark). Could you clarify what you mean by “best”?*
#
# ---
#
# **Example 3**
#    Question: *When was the conference?*
#    Response: *Could you specify which conference you're referring to? The name or acronym is missing.*
#
# ---
#
# **Example 4**
# Question: *Tell me more about it.*
# Response: *Could you clarify what “it” refers to? Please include the full name of the paper or topic.*
#
# ---

prompt_template = """
You are an assistant that checks if a question is complete, specific, and meaningful enough to be answered using a knowledge graph.

Your task is to determine whether a user's question is sufficiently clear for answering, especially in an academic or bibliographic domain (papers, authors, venues, etc.). If the question is vague or incomplete, politely ask the user to rewrite it with more context.


===Examples of complete questions
  Question: what are the papers about embeddings published in 2020 at ACL?
            Who are the authors of Attention is all you need?
            Where did Tim Berners-Lee works?
            Among the papers published in ISWC, which one has the highest citation?
            When was University of Hamburg established?
            Top 10 publications in ISWC.
            Highly cited question answering papers from Web Conf.
            Recent publication of Jens Lehman.
            
            
===Examples of incomplete questions
 Question: What is the best KGQA paper?  
           When was the conference?
           Tell me more about it.
           Who has highest citation?
           Best database publication.
           Best venue.
             
             
===Response Guidelines
When reviewing a user question, first attempt to identify whether the question contains any of the following:
1. An author name
2. A venue or journal name
3. A paper title
4. An institution name

===Response Format
Please respond in below JSON format:
{{
    "completeness": Incomplete or complete,
    "feedback": Your message to the user
}}

===Question
{question}

"""

QUESTION_VALIDATION_PROMPT = PromptTemplate.from_template(prompt_template)