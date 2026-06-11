# backend/prompt_builder.py
# This file creates the detailed instruction (prompt) we send to Gemini

def build_workout_prompt(user_data: dict) -> str:
    """
    Takes user details and creates a clear prompt for Gemini
    to generate a personalized workout plan.
    """
    prompt = f"""
You are an expert personal fitness trainer and certified nutritionist.
Create a highly personalized fitness plan for a student based on the following details:

=== USER PROFILE ===
- Name: {user_data['name']}
- Age: {user_data['age']} years
- Gender: {user_data['gender']}
- Weight: {user_data['weight']} kg
- Height: {user_data['height']} cm
- Fitness Goal: {user_data['goal']}
- Activity Level: {user_data['activity_level']}
- Available Equipment: {user_data['equipment']}
- Days Available for Workout per Week: {user_data['workout_days']}
- Any Health Issues or Injuries: {user_data['health_issues']}

=== GENERATE A 7-DAY WORKOUT PLAN ===
For each day, provide:
1. Day name (e.g., Day 1 - Monday)
2. Focus area (e.g., Upper Body, Cardio, Rest)
3. List of exercises with: exercise name, sets, reps, and rest time
4. Estimated workout duration
5. Warm-up (3 exercises)
6. Cool-down stretches (3 stretches)

Format each day clearly with headers.
Make it realistic for a student with limited time (max 45-60 minutes per session).
Use exercises that match the available equipment.
Include 1-2 rest days in the week.
"""
    return prompt


def build_diet_prompt(user_data: dict) -> str:
    """
    Takes user details and creates a prompt for Gemini
    to generate a personalized diet/meal plan.
    """
    prompt = f"""
You are an expert certified nutritionist specializing in student health.
Create a personalized meal plan for a student based on the following details:

=== USER PROFILE ===
- Name: {user_data['name']}
- Age: {user_data['age']} years
- Gender: {user_data['gender']}
- Weight: {user_data['weight']} kg
- Height: {user_data['height']} cm
- Fitness Goal: {user_data['goal']}
- Activity Level: {user_data['activity_level']}
- Dietary Preference: {user_data['diet_type']}
- Cultural Food Preference: {user_data['food_culture']}
- Food Allergies/Restrictions: {user_data['food_restrictions']}
- Budget: {user_data['budget']} per day

=== GENERATE A 7-DAY MEAL PLAN ===
For each day, provide:
1. Day name
2. Breakfast (with ingredients and portion sizes)
3. Mid-Morning Snack
4. Lunch (with ingredients and portion sizes)
5. Evening Snack
6. Dinner (with ingredients and portion sizes)
7. Total estimated daily calories
8. Protein / Carbs / Fats breakdown

Also include:
- A daily water intake recommendation
- 3 general nutrition tips

Use REALISTIC, AFFORDABLE, and LOCALLY AVAILABLE Indian foods if cultural preference is Indian.
Keep meals simple and student-friendly (easy to cook or buy).
Align calorie intake with the fitness goal.
"""
    return prompt


def build_tips_prompt(user_data: dict) -> str:
    """
    Creates a prompt for motivational tips and health advice.
    """
    prompt = f"""
Give 5 personalized motivational fitness tips and 5 health tips for a {user_data['age']}-year-old 
student whose goal is to {user_data['goal']}.
Their activity level is {user_data['activity_level']}.
Make the tips specific, practical, and encouraging.
Format as numbered lists with bold headings.
Keep language simple and positive.
"""
    return prompt