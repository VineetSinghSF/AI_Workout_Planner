# frontend/app.py
# AI Workout & Diet Planner — Redesigned UI

import streamlit as st
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.planner import generate_workout_plan, generate_diet_plan, generate_tips

# ── Page config ──────────────────────────────────────────────
st.set_page_config(
    page_title="FitAI — Workout & Diet Planner",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── CSS ───────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@400;500;600;700&display=swap');

/* ── Reset & Base ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, .stApp {
    background: #050810 !important;
    font-family: 'Inter', sans-serif;
    color: #e2e8f0;
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container {
    padding: 0 2rem 3rem 2rem !important;
    max-width: 1100px !important;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: #0b0f1a !important;
    border-right: 1px solid #1e2a3a !important;
}
[data-testid="stSidebar"] > div:first-child {
    padding: 1.5rem 1.2rem;
}

/* ── Sidebar labels & text ── */
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] .stSelectbox label,
[data-testid="stSidebar"] .stNumberInput label,
[data-testid="stSidebar"] .stTextInput label,
[data-testid="stSidebar"] .stSlider label,
[data-testid="stSidebar"] .stMultiSelect label {
    color: #94a3b8 !important;
    font-size: 0.78rem !important;
    font-weight: 500 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.06em !important;
}

/* ── Inputs ── */
[data-testid="stSidebar"] input,
[data-testid="stSidebar"] .stSelectbox > div > div {
    background: #111827 !important;
    border: 1px solid #1e2a3a !important;
    border-radius: 8px !important;
    color: #f1f5f9 !important;
    font-size: 0.9rem !important;
}
[data-testid="stSidebar"] input:focus {
    border-color: #22d3ee !important;
    box-shadow: 0 0 0 3px rgba(34,211,238,0.12) !important;
}

/* ── Sidebar section headings ── */
.sidebar-section {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.7rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: #22d3ee;
    margin: 1.4rem 0 0.6rem 0;
    padding-bottom: 0.4rem;
    border-bottom: 1px solid #1e2a3a;
}

/* ── Generate button ── */
.stButton > button {
    background: linear-gradient(135deg, #22d3ee 0%, #6366f1 100%) !important;
    color: #050810 !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
    letter-spacing: 0.03em !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.75rem 1.5rem !important;
    width: 100% !important;
    cursor: pointer !important;
    transition: all 0.25s ease !important;
    margin-top: 0.5rem !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 30px rgba(34,211,238,0.35) !important;
    filter: brightness(1.08) !important;
}
.stButton > button:active {
    transform: translateY(0) !important;
}

/* ── Hero ── */
.hero-wrap {
    padding: 3.5rem 0 2rem 0;
    text-align: center;
}
.hero-badge {
    display: inline-block;
    background: rgba(34,211,238,0.1);
    border: 1px solid rgba(34,211,238,0.3);
    border-radius: 100px;
    padding: 0.3rem 1rem;
    font-size: 0.75rem;
    font-weight: 600;
    color: #22d3ee;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 1.2rem;
}
.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(2.2rem, 5vw, 3.4rem);
    font-weight: 700;
    line-height: 1.1;
    color: #f8fafc;
    margin-bottom: 0.6rem;
    letter-spacing: -0.02em;
}
.hero-title span {
    background: linear-gradient(90deg, #22d3ee, #6366f1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-sub {
    font-size: 1rem;
    color: #64748b;
    font-weight: 400;
    max-width: 480px;
    margin: 0 auto 2rem auto;
    line-height: 1.6;
}

/* ── Stat pills ── */
.stats-row {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 0.6rem;
    margin-bottom: 2rem;
}
.stat-pill {
    background: #0f1623;
    border: 1px solid #1e2a3a;
    border-radius: 100px;
    padding: 0.45rem 1.1rem;
    font-size: 0.8rem;
    color: #94a3b8;
    font-weight: 500;
}
.stat-pill strong { color: #e2e8f0; }

/* ── Divider ── */
.divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, #1e2a3a, transparent);
    margin: 1.5rem 0;
}

/* ── Feature cards (welcome screen) ── */
.feature-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
    margin: 1.5rem 0;
}
.feature-card {
    background: #0b0f1a;
    border: 1px solid #1e2a3a;
    border-radius: 16px;
    padding: 1.5rem;
    transition: border-color 0.2s, transform 0.2s;
}
.feature-card:hover {
    border-color: #22d3ee40;
    transform: translateY(-3px);
}
.fc-icon {
    font-size: 1.8rem;
    margin-bottom: 0.8rem;
}
.fc-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.95rem;
    font-weight: 600;
    color: #f1f5f9;
    margin-bottom: 0.4rem;
}
.fc-desc {
    font-size: 0.82rem;
    color: #475569;
    line-height: 1.55;
}

/* ── Prompt banner ── */
.prompt-banner {
    background: linear-gradient(135deg, #0f1a2e, #111827);
    border: 1px solid #1e3a5f;
    border-left: 3px solid #22d3ee;
    border-radius: 0 12px 12px 0;
    padding: 1rem 1.4rem;
    margin: 1rem 0 1.5rem 0;
    font-size: 0.88rem;
    color: #94a3b8;
    line-height: 1.5;
}
.prompt-banner strong { color: #22d3ee; }

/* ── Profile summary banner (after generate) ── */
.profile-bar {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin: 1rem 0 1.5rem 0;
}
.profile-chip {
    background: #0f1623;
    border: 1px solid #1e2a3a;
    border-radius: 8px;
    padding: 0.3rem 0.75rem;
    font-size: 0.78rem;
    color: #94a3b8;
}
.profile-chip b { color: #e2e8f0; }

/* ── Tabs ── */
[data-testid="stTabs"] [data-baseweb="tab-list"] {
    background: #0b0f1a !important;
    border-bottom: 1px solid #1e2a3a !important;
    gap: 0 !important;
    border-radius: 12px 12px 0 0 !important;
    padding: 0 0.5rem !important;
}
[data-testid="stTabs"] [data-baseweb="tab"] {
    background: transparent !important;
    color: #475569 !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.88rem !important;
    padding: 0.75rem 1.2rem !important;
    border-bottom: 2px solid transparent !important;
    border-radius: 0 !important;
}
[data-testid="stTabs"] [aria-selected="true"] {
    color: #22d3ee !important;
    border-bottom: 2px solid #22d3ee !important;
    background: transparent !important;
}

/* ── Plan output card ── */
.plan-output {
    background: #0b0f1a;
    border: 1px solid #1e2a3a;
    border-radius: 0 0 16px 16px;
    padding: 2rem;
    font-size: 0.9rem;
    line-height: 1.75;
    color: #cbd5e1;
    white-space: pre-wrap;
    word-wrap: break-word;
    min-height: 200px;
}

/* ── Download button ── */
[data-testid="stDownloadButton"] button {
    background: #111827 !important;
    color: #22d3ee !important;
    border: 1px solid #1e3a5f !important;
    border-radius: 8px !important;
    font-size: 0.82rem !important;
    font-weight: 600 !important;
    padding: 0.45rem 1rem !important;
    width: auto !important;
    margin-top: 0.8rem !important;
    transition: all 0.2s !important;
}
[data-testid="stDownloadButton"] button:hover {
    background: #1e2a3a !important;
    transform: none !important;
    box-shadow: none !important;
}

/* ── Spinner ── */
[data-testid="stSpinner"] { color: #22d3ee !important; }

/* ── Success ── */
.stSuccess {
    background: rgba(34,211,238,0.08) !important;
    border: 1px solid rgba(34,211,238,0.25) !important;
    border-radius: 10px !important;
    color: #22d3ee !important;
}

/* ── Error ── */
.stAlert[data-baseweb="notification"] {
    background: rgba(239,68,68,0.08) !important;
    border: 1px solid rgba(239,68,68,0.25) !important;
    border-radius: 10px !important;
}

/* ── Slider ── */
[data-testid="stSlider"] [data-baseweb="slider"] [data-testid="stThumbValue"] {
    color: #22d3ee !important;
}

/* ── Footer ── */
.footer {
    text-align: center;
    font-size: 0.75rem;
    color: #1e2a3a;
    padding: 2rem 0 1rem 0;
    letter-spacing: 0.02em;
}

/* Responsive */
@media (max-width: 768px) {
    .feature-grid { grid-template-columns: 1fr; }
    .hero-title { font-size: 1.8rem; }
}
</style>
""", unsafe_allow_html=True)


# ── Sidebar ───────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="display:flex;align-items:center;gap:0.6rem;margin-bottom:0.3rem;">
        <span style="font-size:1.3rem;">⚡</span>
        <span style="font-family:'Space Grotesk',sans-serif;font-size:1rem;
                     font-weight:700;color:#f1f5f9;letter-spacing:-0.01em;">FitAI</span>
    </div>
    <div style="font-size:0.75rem;color:#334155;margin-bottom:1.2rem;">
        Powered by Google Gemini
    </div>
    """, unsafe_allow_html=True)

    # ── Personal Info ──
    st.markdown('<div class="sidebar-section">👤 Personal Info</div>', unsafe_allow_html=True)
    name = st.text_input("Full Name", placeholder="e.g. Rahul Sharma", label_visibility="visible")
    c1, c2 = st.columns(2)
    with c1:
        age = st.number_input("Age", 10, 80, 20)
    with c2:
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    c3, c4 = st.columns(2)
    with c3:
        weight = st.number_input("Weight (kg)", 30.0, 200.0, 65.0, 0.5)
    with c4:
        height = st.number_input("Height (cm)", 100, 250, 170)

    # ── Fitness ──
    st.markdown('<div class="sidebar-section">🎯 Fitness Goals</div>', unsafe_allow_html=True)
    goal = st.selectbox("Primary Goal", [
        "Lose Weight / Fat Loss",
        "Gain Muscle / Bulk Up",
        "Stay Fit / Maintain Weight",
        "Improve Stamina / Endurance",
        "Improve Flexibility"
    ])
    activity_level = st.selectbox("Activity Level", [
        "Sedentary — little to no exercise",
        "Lightly Active — 1–2 days/week",
        "Moderately Active — 3–4 days/week",
        "Very Active — 5–6 days/week",
        "Athlete — daily intense training"
    ])
    workout_days = st.slider("Workout days per week", 1, 7, 4)
    equipment = st.multiselect("Available Equipment", [
        "Bodyweight only", "Dumbbells", "Resistance Bands",
        "Pull-up Bar", "Gym Access", "Treadmill", "Yoga Mat"
    ], default=["Bodyweight only"])
    health_issues = st.text_input("Injuries / Health issues", placeholder="e.g. knee pain (optional)")

    # ── Diet ──
    st.markdown('<div class="sidebar-section">🥗 Diet Preferences</div>', unsafe_allow_html=True)
    diet_type = st.selectbox("Dietary Type", [
        "Non-Vegetarian", "Vegetarian", "Vegan", "Eggetarian", "Pescatarian"
    ])
    food_culture = st.selectbox("Food Culture", [
        "Indian (North Indian)", "Indian (South Indian)", "Indian (General)",
        "Western", "Mediterranean", "Asian", "No Preference"
    ])
    food_restrictions = st.text_input("Allergies / Restrictions", placeholder="e.g. no dairy (optional)")
    budget = st.selectbox("Daily Food Budget", [
        "Low — ₹100–200/day", "Medium — ₹200–400/day", "High — ₹400+/day"
    ])

    st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)
    generate_btn = st.button("⚡ Generate My Plan", use_container_width=True)


# ── Main ──────────────────────────────────────────────────────

# Hero
st.markdown("""
<div class="hero-wrap">
    <div class="hero-badge">⚡ AI-Powered Fitness</div>
    <h1 class="hero-title">Your Personal<br><span>Workout & Diet Plan</span></h1>
    <p class="hero-sub">
        Tell us about yourself. Gemini AI builds a 7-day workout routine
        and meal plan that fits your life — your budget, your food, your goals.
    </p>
</div>
""", unsafe_allow_html=True)

# ── Welcome state ──
if not generate_btn:
    st.markdown("""
    <div class="prompt-banner">
        <strong>👈 Fill in your profile</strong> in the sidebar, then hit
        <strong>Generate My Plan</strong> — takes about 30 seconds.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-grid">
        <div class="feature-card">
            <div class="fc-icon">💪</div>
            <div class="fc-title">7-Day Workout Plan</div>
            <div class="fc-desc">Sets, reps, rest times, warm-up and cool-down — built around your equipment and schedule.</div>
        </div>
        <div class="feature-card">
            <div class="fc-icon">🥗</div>
            <div class="fc-title">Custom Meal Plan</div>
            <div class="fc-desc">Culturally relevant, budget-friendly meals with full calorie and macro breakdown per day.</div>
        </div>
        <div class="feature-card">
            <div class="fc-icon">💡</div>
            <div class="fc-title">Personalised Tips</div>
            <div class="fc-desc">Motivational advice and health tips tailored to your age, goal, and activity level.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="divider"></div>
    <div style="display:flex;justify-content:center;gap:3rem;flex-wrap:wrap;
                margin:1.5rem 0;color:#334155;font-size:0.82rem;text-align:center;">
        <div><div style="font-size:1.6rem;font-weight:800;color:#22d3ee;
             font-family:'Space Grotesk',sans-serif;">7</div>day plans</div>
        <div><div style="font-size:1.6rem;font-weight:800;color:#6366f1;
             font-family:'Space Grotesk',sans-serif;">3</div>output tabs</div>
        <div><div style="font-size:1.6rem;font-weight:800;color:#22d3ee;
             font-family:'Space Grotesk',sans-serif;">100%</div>personalised</div>
        <div><div style="font-size:1.6rem;font-weight:800;color:#6366f1;
             font-family:'Space Grotesk',sans-serif;">Free</div>to use</div>
    </div>
    """, unsafe_allow_html=True)


# ── Generated state ──
if generate_btn:
    if not name.strip():
        st.error("Please enter your name in the sidebar before generating.")
        st.stop()

    user_data = {
        "name": name,
        "age": age,
        "gender": gender,
        "weight": weight,
        "height": height,
        "goal": goal,
        "activity_level": activity_level,
        "workout_days": workout_days,
        "equipment": ", ".join(equipment) if equipment else "Bodyweight only",
        "health_issues": health_issues or "None",
        "diet_type": diet_type,
        "food_culture": food_culture,
        "food_restrictions": food_restrictions or "None",
        "budget": budget,
    }

    # Greeting + profile chips
    st.markdown(f"""
    <div style="margin-bottom:0.5rem;">
        <span style="font-family:'Space Grotesk',sans-serif;font-size:1.4rem;
                     font-weight:700;color:#f8fafc;">Hey {name} 👋</span>
        <span style="font-size:0.85rem;color:#475569;margin-left:0.7rem;">
            Here's your personalised plan
        </span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="profile-bar">
        <div class="profile-chip"><b>⚖️</b> {weight} kg</div>
        <div class="profile-chip"><b>📏</b> {height} cm</div>
        <div class="profile-chip"><b>🎯</b> {goal}</div>
        <div class="profile-chip"><b>🏃</b> {activity_level.split('—')[0].strip()}</div>
        <div class="profile-chip"><b>🥗</b> {diet_type}</div>
        <div class="profile-chip"><b>🍛</b> {food_culture}</div>
        <div class="profile-chip"><b>📅</b> {workout_days} days/week</div>
    </div>
    <div class="divider"></div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["💪  Workout Plan", "🥗  Meal Plan", "💡  Tips & Advice"])

    with tab1:
        with st.spinner("Building your workout plan…"):
            workout = generate_workout_plan(user_data)
        st.markdown(f'<div class="plan-output">{workout}</div>', unsafe_allow_html=True)
        st.download_button(
            "📥 Download Workout Plan",
            data=workout,
            file_name=f"{name.replace(' ','_')}_workout_plan.txt",
            mime="text/plain"
        )

    with tab2:
        with st.spinner("Building your meal plan…"):
            diet = generate_diet_plan(user_data)
        st.markdown(f'<div class="plan-output">{diet}</div>', unsafe_allow_html=True)
        st.download_button(
            "📥 Download Meal Plan",
            data=diet,
            file_name=f"{name.replace(' ','_')}_meal_plan.txt",
            mime="text/plain"
        )

    with tab3:
        with st.spinner("Generating your tips…"):
            tips = generate_tips(user_data)
        st.markdown(f'<div class="plan-output">{tips}</div>', unsafe_allow_html=True)

    st.success("✅ All plans generated! Switch between the tabs above to explore.")
    st.balloons()


# ── Footer ──
st.markdown("""
<div class="footer">
    FitAI · Built with Streamlit + Google Gemini &nbsp;·&nbsp;
    For educational purposes only — consult a professional for medical advice.
</div>
""", unsafe_allow_html=True)