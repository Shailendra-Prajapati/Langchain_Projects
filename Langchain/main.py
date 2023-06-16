# integrate our code with OpenAI API

import os
from constants import openai_key
from langchain.llms import OpenAI


import streamlit as st

os.environ["OPENAI_API_KEY"]=openai_key

#Streamlit Framework

st.title("Langchain With OpenAI API")
input_text=st.text_input("Search the topic you want")

## OpenAI LLM
llm=OpenAI(temperature=0.8) #Control of Agent over response

if input_text:
    st.write(llm(input_text))
    
    