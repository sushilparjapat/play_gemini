from dotenv import load_dotenv
load_dotenv()
import streamlit as st

import os


import google.generativeai as genai

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

def get_gemini_model_response(question):
    if input != "" :
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(question)
        return response.text
    else:
        return "Please ask Question"

st.set_page_config(page_title = "Play with Gemini")
st.header("Gemini Application")
input = st.text_input("Input: " , key = "input")

submit = st.button("Ask Question")

if submit:
    response = get_gemini_model_response(input)
    st.subheader("The Response is : ")
    st.write(response)
