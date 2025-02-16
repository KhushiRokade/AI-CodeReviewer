import streamlit as st
import google.generativeai as genai
import os
import time

# Secure API Key Retrieval
API_KEY = os.getenv("GEMINI_API_KEY")  # Ensure the API key is securely stored in environment variables

if not API_KEY:
    st.error("API Key is missing. Please set it in your environment variables.")
    st.stop()
else:
    try:
        genai.configure(api_key=API_KEY)
    except Exception as e:
        st.error(f"Error configuring API key: {e}")
        st.stop()

# Define System Prompt
sys_prompt = """
You are an advanced Python code reviewer. Your task is to analyze the given Python code, 
identify potential bugs, logical errors, inefficiencies, and areas of improvement, and suggest fixes.

Your response should be structured as follows:
1. *Issues Detected*: List any errors, inefficiencies, or improvements needed.
2. *Fixed Code*: Provide the corrected version of the code.
3. *Explanation*: Explain why the changes were made concisely.

If the code is already optimal, acknowledge it and suggest best practices.
"""

def code_review(code):
    """Sends user code to Google Gemini AI for review and returns feedback."""
    try:
        time.sleep(1)
        model = genai.GenerativeModel("gemini-1.5-pro", system_instruction=sys_prompt)
        user_prompt = f"Review the following Python code and provide feedback on potential bugs, improvements, and fixes:\n\n{code}"
        response = model.generate_content(user_prompt)
        return response.text
    except Exception as e:
        return f"Error during code review: {e}"

# Streamlit UI Setup
st.set_page_config(page_title="Python Code Reviewer", page_icon="🤖", layout="wide")
st.title("🤖 Python Code Reviewer")
st.markdown("### Analyze your Python code for bugs, optimizations, and improvements!")

# Sidebar
st.sidebar.header("Navigation")
st.sidebar.markdown("Use this tool to analyze Python code and receive AI-powered feedback.")
st.sidebar.markdown("---")

# User Input
code_input = st.text_area("Enter your Python code:", height=250)
uploaded_file = st.file_uploader("Or upload a Python file:", type=["py"])

if uploaded_file is not None:
    try:
        code_input = uploaded_file.read().decode("utf-8")
        st.text_area("Uploaded File Content:", code_input, height=250, disabled=True)
    except Exception as e:
        st.error(f"Error reading file: {e}")

# Review Button
if st.button("🔍 Review Code"):
    if code_input.strip():
        with st.spinner("Analyzing your code with Google AI..."):
            feedback = code_review(code_input)
        
        # Display AI Feedback
        st.subheader("📋 Code Review Report")
        st.markdown(feedback)
    else:
        st.warning("Please enter some Python code before submitting.")
