import os 
import streamlit as st
import google.generativeai as genai

Api_Key = os.getenv("GEMINI_API_KEY")

if not Api_Key:
  st.error("API key is missing. Please set it in your environment variables.")
else:
  genai.configure(api_key = Api_Key )

#Define the system prompt