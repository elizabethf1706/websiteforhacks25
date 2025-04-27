import streamlit as st

# Set the title of the app
st.title("Conversation Summary")

# Assume the summary is already given
summary_text = "This is a sample summary provided directly in the code. Until we configure that, this is just a text placeholder"

# Display the given summary
st.subheader("Your Summary:")
st.write(summary_text)
