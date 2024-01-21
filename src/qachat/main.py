from dotenv import load_dotenv
import os
import google.generativeai as genai

import streamlit as st

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def get_gemini_resp(chat, question):
    response = chat.send_message(question, stream=True)
    return response

def main():
    model = genai.GenerativeModel("gemini-pro")
    chat  = model.start_chat(history=[])

    st.set_page_config(page_title='Q&A Demo')

    st.header("Hemini LLM App")

    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []
    
    input = st.text_input("Input:", key="input")

    submit = st.button("Ask the Question")

    if submit and input :
        response = get_gemini_resp(chat, input)
        st.session_state['chat_history'].append(("you", input))
        st.subheader("The Response is")

        for chunk in response:
            st.write(chunk.text)
            st.session_state['chat_history'].append(("bot", chunk.text))

    st.subheader("Chat History")

    for role, text in st.session_state['chat_history']:
        st.write(f"{role} : {text}")


if __name__ == '__main__':
    load_dotenv()
    main()