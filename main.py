import streamlit as st
import groq
import re
import requests
import fitz  # PyMuPDF
import mammoth  # For DOCX reading
from io import BytesIO

# Set the title
st.set_page_config(page_title="PDF/DOCX to Text", page_icon="📄", layout="centered")
st.title("Business Networking Follow-Up Generator")

uploaded_file = st.file_uploader("Upload your file", type=["pdf", "docx"])

# Extract text functions
def extract_text_from_pdf(file):
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text.strip()

def extract_text_from_docx(file):
    result = mammoth.extract_raw_text(file)
    return result.value.strip()

# Function to send resume to backend
def send_resume_to_backend(resume_text):
    try:
        response = requests.post(
            "https://la-hacks-2025-backend.onrender.com/api/set_resume",
            json={"resume": resume_text}
        )
        response.raise_for_status()
        return True
    except Exception as e:
        st.error(f"Failed to send resume: {e}")
        return False

if uploaded_file:
    file_type = uploaded_file.type

    with st.spinner('Processing...'):
        if file_type == "application/pdf" or uploaded_file.name.endswith(".pdf"):
            extracted_text = extract_text_from_pdf(uploaded_file)
        elif uploaded_file.name.endswith(".docx"):
            extracted_text = extract_text_from_docx(uploaded_file)
        else:
            extracted_text = None

    if extracted_text:
        st.success("✅ Text extracted successfully!")
        st.text_area("Extracted Text:", extracted_text, height=300)

        # Automatically send to backend
        with st.spinner('Sending resume to backend...'):
            success = send_resume_to_backend(extracted_text)
            if success:
                st.success("✅ Resume sent to backend successfully!")
            else:
                st.error("⚠️ Failed to send resume to backend.")

    else:
        st.error("⚠️ Unsupported file type or failed to extract text.")

# -- the rest of your conversation and follow-up generation logic --
# (you can keep your fetch_conversation(), make_links_clickable(), analyze_summary(), etc., as you have them.)
