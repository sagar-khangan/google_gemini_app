from urllib import response
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel("gemini-pro")

def get_gemini_resp(question):    
    response = model.generate_content(question)
    print(response.candidates)
    print(response.prompt_feedback)
    return response.text    

def main ():
    st.set_page_config(page_title="Q&A demo")
    st.header("Gemini LLM App")
    input = st.text_input("Input", key="input")
    submit = st.button("Get Answer")

    if submit : 
        response = get_gemini_resp(input)
        st.subheader("The response is")
        st.write(response)

if __name__ == '__main__':
    main()