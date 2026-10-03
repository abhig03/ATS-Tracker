import os
import io
# from dotenv import load_dotenv
import streamlit as st
from PIL import Image 
import pdf2image
from google import genai

# Load environment variables
# load_dotenv()

# Configuration
# model_id = 'gemini-2.5-flash'

if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
else:
    # For local testing, ensure you run 'export GOOGLE_API_KEY=...' in your terminal before running streamlit
    api_key = os.getenv("GOOGLE_API_KEY")

model_id = 'gemini-3.8-flash'

# Note: The new SDK looks for GEMINI_API_KEY by default, but you can pass GOOGLE_API_KEY explicitly
client = genai.Client(api_key=api_key)

def get_gemini_response(input_text, pdf_content, prompt):
    # pdf_content[0] is now a raw PIL Image object, which the SDK accepts natively
    response = client.models.generate_content(
        model=model_id,
        contents=[input_text, pdf_content[0], prompt]
    )
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Convert PDF to list of PIL images
        images = pdf2image.convert_from_bytes(
            uploaded_file.read()
        )
        
        # Get the first page directly as a PIL Image object
        first_page = images[0]
        
        # Simply return the image object wrapped in a list
        return [first_page]
    else:
        raise FileNotFoundError("No File Uploaded")

# --- Streamlit UI App Setup ---
st.set_page_config(page_title='ATS Resume Tracker')
st.header("ATS Resume Tracker")

input_text = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload your Resume (PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF uploaded successfully")

submit1 = st.button("Tell me about the Resume")
submit3 = st.button("Percentage match")

input_prompt1 = """
You are an experienced Technical Human Resource Manager, your task is to review the provided resume against the job description. 
Please share your professional evaluation on whether the candidate's profile aligns with the role. 
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of tech roles and ATS functionality, 
your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

if submit1:
    if uploaded_file is not None:
        with st.spinner("Analyzing resume..."):
            pdf_content = input_pdf_setup(uploaded_file)
            response = get_gemini_response(input_prompt1, pdf_content, input_text)
            st.header("The Response is: ")
            st.write(response)
    else:
        st.write("Please upload Resume")

elif submit3:
    if uploaded_file is not None:
        with st.spinner("Calculating match percentage..."):
            pdf_content = input_pdf_setup(uploaded_file)
            response = get_gemini_response(input_prompt3, pdf_content, input_text)
            st.header("The Response is: ")
            st.write(response)
    else:
        st.write("Please upload Resume")
