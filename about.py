import streamlit as st

st.set_page_config(page_title="About", page_icon="ℹ️", layout="centered")

st.title("About This App")
st.write("""
Welcome to the **Business Networking Follow-Up Generator**! 📄✨

This app helps you:
- Upload your resume (PDF/DOCX)
- Extract text automatically
- Get personalized career coaching feedback powered by **Gemini AI**.

Built with ❤️ using Streamlit and Google Gemini API.
""")
