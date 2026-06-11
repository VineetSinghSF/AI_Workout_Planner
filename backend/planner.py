# backend/planner.py
# This is the main backend logic — it calls Gemini and returns the plans

from backend.gemini_client import get_gemini_model
from backend.prompt_builder import build_workout_prompt, build_diet_prompt, build_tips_prompt
import time

def generate_workout_plan(user_data: dict) -> str:
    """
    Generates a personalized 7-day workout plan using Gemini AI.
    Returns the plan as a formatted string.
    """
    try:
        time.sleep(2)
        model = get_gemini_model()
        prompt = build_workout_prompt(user_data)
        
        response = model.generate_content(prompt)
        return response.text
    
    except Exception as e:
        return f"Error generating workout plan: {str(e)}"


def generate_diet_plan(user_data: dict) -> str:
    """
    Generates a personalized 7-day diet/meal plan using Gemini AI.
    Returns the plan as a formatted string.
    """
    try:
        time.sleep(2)
        model = get_gemini_model()
        prompt = build_diet_prompt(user_data)
        
        response = model.generate_content(prompt)
        return response.text
    
    except Exception as e:
        return f"Error generating diet plan: {str(e)}"


def generate_tips(user_data: dict) -> str:
    """
    Generates personalized fitness tips using Gemini AI.
    """
    try:
        time.sleep(2)
        model = get_gemini_model()
        prompt = build_tips_prompt(user_data)
        
        response = model.generate_content(prompt)
        return response.text
    
    except Exception as e:
        return f"Error generating tips: {str(e)}"