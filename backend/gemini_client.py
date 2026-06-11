# backend/gemini_client.py
# This file sets up the connection to Google Gemini AI

import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv()

def get_gemini_model():
    """
    Connects to Gemini and returns the AI model ready to use.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found! Check your .env file.")
    
    # Configure Gemini with your API key
    genai.configure(api_key=api_key)
    
    # Use Gemini 1.5 Flash (fast and free)
    model = genai.GenerativeModel("gemini-2.5-flash")
    
    return model