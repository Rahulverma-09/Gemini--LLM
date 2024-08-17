# GEMINI LLM APPLICATION--

#Loading Environment Variable
from dotenv import load_dotenv
load_dotenv()

#Required Libraries
import os
import streamlit as st
import google.generativeai as genai

#Configuration of API_KEY
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Load Gemini-Pro-Model
model=genai.GenerativeModel('gemini-pro')

#Function to get question and generate some respose
def get_response(question):
    response = model.generate_content(question)
    return response.text

#setup streamlit app--
st.set_page_config(page_title="streamlit app")

st.header("Quick Response Application")

input=st.text_input("Input:", key="input")
submit=st.button("Ask the question")

#If button is clicked--
if submit:
    response=get_response(input)
    st.subheader("The Response is")
    st.write(response)