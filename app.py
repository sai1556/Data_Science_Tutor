import streamlit as st
import google.generativeai as genai

# Set API Key securely
GOOGLE_API_KEY = "AIzaSyAlCtdrEW48j2rPrVaBtmEEebaxDf-qf8M"  # Store in environment variable
if not GOOGLE_API_KEY:
    st.error("API Key is missing! Please set the GOOGLE_API_KEY environment variable.")
    st.stop()

genai.configure(api_key=GOOGLE_API_KEY)

# Function to get AI response
def get_gemini_response(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")  # Ensure correct model name
        response = model.generate_content(prompt)
        return response.text if hasattr(response, "text") else "No response received."
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.title("AI-Powered Data Science Tutor 📊")

# User input
user_input = st.text_area("Ask me any Data Science-related question, and I'll provide Python implementations where applicable!", "")

if st.button("Submit") and user_input:
    with st.spinner("stay tuned..."):
        response = get_gemini_response(user_input)
    st.success("Response Generated Successfully!")
    st.subheader("AI's Response:")
    st.write(response)
