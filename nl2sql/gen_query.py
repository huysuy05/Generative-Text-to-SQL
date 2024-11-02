import requests
import json
from nl2sql.extract_sql import *
import os
import openai
OPENROUTER_API_KEY = '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'
openai.api_base = "https://openrouter.ai/api/v1"
openai.api_key = OPENROUTER_API_KEY

def glob_context(new_context):
    global context
    context = new_context
    return context
def gen_prompt_query(question):
    return f"""
    Welcome to a TEXT-to-SQL where you can ask a question about the data and the program will generate a query for you
    
    *** Question:
    {question}
    
    *** Output:
    {context}
    """

def gen_sql_query(question):
    prompt = gen_prompt_query(question)
    response = openai.ChatCompletion.create(
            model= 'gpt-4o',
            messages = [{"role": "user", "content": prompt}]
    )
    raw_query = response['choices'][0]['message']['content']
    query = extract_sql(raw_query)
    return query

    