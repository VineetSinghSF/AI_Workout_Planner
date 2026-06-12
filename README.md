# 🏋️ AI-Powered Personalized Workout & Diet Planner

An AI-powered web application that generates personalized workout routines and diet plans based on individual user preferences, fitness goals, dietary habits, and available resources.

Developed as part of the **IBM SkillsBuild Internship Capstone Project**.

---

## 🚀 Live Demo

🔗 Deployment Link:
https://aiworkoutplanner-rrgpsncajy9agrvqhiewqd.streamlit.app/

🔗 GitHub Repository:
https://github.com/VineetSinghSF/AI_Workout_Planner

---

## 📌 Problem Statement

Most fitness applications provide generic workout routines and diet plans that fail to consider:

- Individual fitness goals
- Body measurements
- Dietary preferences
- Cultural food habits
- Available workout resources
- Budget constraints

As a result, users often receive recommendations that are impractical, difficult to follow, and less effective.

### Proposed Solution

This project provides an AI-powered fitness planner that generates personalized workout and diet recommendations according to the user's profile, preferences, and goals.

---

## ✨ Features

### User Inputs

- Age
- Gender
- Height
- Weight
- Fitness Goal
- Activity Level
- Diet Preference
- Food Culture
- Budget
- Available Equipment
- Health Conditions

### AI Outputs

- Personalized Workout Plan
- Customized Diet Plan
- Nutrition Suggestions
- Fitness Recommendations
- Healthy Lifestyle Tips

---

## 🛠️ Technology Stack

### Frontend
- Streamlit

### Backend
- Python

### AI Integration
- Google Gemini API

### Development Tools
- Visual Studio Code
- GitHub

### Deployment
- Streamlit Community Cloud

### Libraries Used
- streamlit
- google-generativeai
- python-dotenv
- pandas

---

## 🏗️ Project Architecture

```text
User
   │
   ▼
Streamlit Frontend
   │
   ▼
Input Processing
   │
   ▼
Prompt Generation
   │
   ▼
Google Gemini AI
   │
   ▼
Workout & Diet Generation
   │
   ▼
Results Display
```

---

## ⚙️ Workflow

1. User enters personal fitness information.
2. System validates the inputs.
3. A structured prompt is generated.
4. User data is sent to Gemini AI.
5. AI generates a personalized workout plan.
6. AI generates a personalized diet plan.
7. Results are displayed through the Streamlit interface.

---

## 📂 Project Structure

```text
AI_Workout_Planner/
│
├── frontend/
│   └── app.py
│
├── backend/
│   ├── planner.py
│   ├── gemini_client.py
│   └── helper_functions.py
│
├── assets/
│
├── requirements.txt
│
├── .env
│
└── README.md
```

---

## 💻 Installation

### Clone Repository

```bash
git clone https://github.com/VineetSinghSF/AI_Workout_Planner.git
```

### Move to Project Directory

```bash
cd AI_Workout_Planner
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file and add:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Get your Gemini API Key from:

https://aistudio.google.com/

---

## ▶️ Run Locally

```bash
streamlit run frontend/app.py
```

Then open:

```text
http://localhost:8501
```

---

## 📊 Results

The application successfully generates personalized workout and diet plans according to user goals, dietary preferences, lifestyle, and budget.

### Achievements

✅ Personalized Workout Generation

✅ Customized Diet Planning

✅ AI-Based Recommendations

✅ User-Friendly Interface

✅ Cloud Deployment

✅ Real-Time Fitness Guidance

---

## 🔮 Future Scope

- BMI and Body Fat Analysis
- Progress Tracking Dashboard
- Weekly Fitness Reports
- AI Fitness Chatbot
- Voice-Based Assistance
- Mobile Application
- Wearable Device Integration
- Real-Time Nutrition Tracking
- Multi-Language Support

---

## 🎯 Conclusion

The AI-Powered Personalized Workout & Diet Planner successfully addresses the limitations of traditional fitness applications by providing customized workout and nutrition recommendations.

Using Google Gemini AI and Streamlit, the project delivers an intelligent, interactive, and user-friendly fitness planning experience.

---

## 📚 References

- Google Gemini API Documentation
- Streamlit Documentation
- Python Documentation
- GitHub Documentation
- IBM SkillsBuild Learning Resources
- Scikit-Learn Documentation
- Hugging Face Community

---

## 👨‍💻 Author

**Vineet Singh**

B.Tech CSE (AI & ML)

KIET Group of Institutions

IBM SkillsBuild Internship Project

---

⭐ If you found this project useful, please consider giving it a star on GitHub.
