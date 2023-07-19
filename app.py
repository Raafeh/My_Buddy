# import os 
from dotenv import load_dotenv
from apikey import api_key

# import streamlit as st
from langchain import HuggingFaceHub, LLMChain
from langchain.prompts import PromptTemplate

# os.environ['HuggingFaceHub_API_KEY'] = api_key

load_dotenv()

hub_llm=HuggingFaceHub(repo_id='mrm8488/t5-base-finetuned-wikiSQL',model_kwargs={'temperature':0.8,'max_length':100} )

prompt= PromptTemplate(
    input_variables=['question'],
    template='Translate English to SQL: {question}',
)

hub_chain=LLMChain(prompt=prompt, llm=hub_llm , verbose=True)

print(hub_chain.run('What is the average age of students in a class?'))
