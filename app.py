import os
import io
# from dotenv import load_dotenv
import streamlit as st
from PIL import Image 
import pdf2image
from google import genai


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
Role: You are an expert Human Resource Manager and Talent Acquisition Specialist across diverse industries.
Task: Conduct a rigorous professional evaluation of the provided resume against the given job description.

Instructions:
1. Assess the overall alignment between the candidate's professional profile and the requirements of the role.
2. Provide a detailed breakdown of the applicant's core strengths (skills, experiences, or achievements that match the role).
3. Identify specific gaps or weaknesses where the candidate's profile falls short of the job criteria.
4. Conclude with a definitive summary stating whether the candidate is a strong, moderate, or weak fit for the position.

Maintain an objective, constructive, and highly professional corporate tone.
"""


input_prompt3 = """
Role: You are an advanced Applicant Tracking System (ATS) optimization scanner calibrated for global hiring standards across all professional industries.
Task: Evaluate the text/image of the resume against the provided job description to determine structural and contextual alignment.

Strict Output Format Requirements:
Your response must follow this exact layout down to the headers:

### 1. ATS Match Percentage
[Provide a realistic percentage match score between 0% and 100% based on skill matching, experience levels, and domain alignment.]

### 2. Missing Keywords & Skills
- [List critical hard skills, tools, methodologies, or certifications mentioned in the job description that are completely missing from the resume.]
- [List relevant soft skills or domain-specific terminology that should be incorporated.]

### 3. Final Strategic Thoughts
[Provide a concise, data-driven analysis of why the score was given, and offer 2-3 actionable recommendations on how the candidate can modify their resume layout or phrasing to improve their ATS visibility for this specific type of role.]
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
