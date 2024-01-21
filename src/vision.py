from urllib import response
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel("gemini-pro-vision")


def get_gemini_resp(input, image):    
    if input != "":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    print(response.candidates)
    print(response.prompt_feedback)
    return response.text    



def main():

    st.set_page_config(page_title="Image demo")
    st.header("Gemini LLM App")
    input = st.text_input("Input", key="input")

    st.title("Image Uploader")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])  # You can specify the allowed file types

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.write("")
        st.write("Classifying...")  
        submit = st.button("Get Answer")
        if submit : 
            response = get_gemini_resp(input, image)
            st.subheader("The response is")
            st.write(response)


if __name__ == "__main__":
    main()
