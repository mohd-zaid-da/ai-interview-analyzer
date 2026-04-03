#AI INTERVIEW ANALYZER (HYBRID VERSION)

import streamlit as st
import time
import pandas as pd
import json
import random

#OpenAI
try:
    from openai import OpenAI
    client = OpenAI(api_key="YOUR_OPENAI_API_KEY")  # optional
    USE_AI = True
except:
    USE_AI = False

#CONFIG
st.set_page_config(page_title="AI Interview Analyzer", layout="wide")

#DATABASE
USER_FILE = "users.json"

def load_users():
    try:
        with open(USER_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f)

#AUTH
def signup(username, password):
    users = load_users()
    if username in users:
        return False
    users[username] = password
    save_users(users)
    return True

def login(username, password):
    users = load_users()
    return username in users and users[username] == password

# SESSION STATE
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = None

# LOGIN UI
if not st.session_state.logged_in:

    st.title(" Login / Signup")

    tab1, tab2 = st.tabs(["Login", "Signup"])

    with tab1:
        u = st.text_input("Username")
        p = st.text_input("Password", type="password")

        if st.button("Login"):
            if login(u, p):
                st.session_state.logged_in = True
                st.session_state.user = u
                st.rerun()
            else:
                st.error("Invalid credentials")

    with tab2:
        u = st.text_input("New Username")
        p = st.text_input("New Password", type="password")

        if st.button("Signup"):
            if signup(u, p):
                st.success("Account created")
            else:
                st.error("User exists")

    st.stop()

#MAIN APP

st.title(f"🎯 Welcome {st.session_state.user}")

#Sidebar
with st.sidebar:
    role = st.selectbox("Role", ["Python Developer", "Data Analyst"])
    difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

#SESSION STATE
if "question" not in st.session_state:
    st.session_state.question = None
    st.session_state.start_time = time.time()

if "history" not in st.session_state:
    st.session_state.history = []

#HYBRID QUESTION GEN.
def generate_question(role, difficulty):
    if USE_AI:
        try:
            prompt = f"Generate one {difficulty} level interview question for {role}."

            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[{"role": "user", "content": prompt}]
            )

            return response.choices[0].message.content.strip()
        except:
            pass  # fallback

    # fallback questions
    fallback = {
        "Python Developer": [
            "What is list vs tuple?",
            "Explain OOP concepts",
            "What is a function in Python?"
        ],
        "Data Analyst": [
            "What is data cleaning?",
            "What is correlation?",
            "Explain mean vs median"
        ]
    }

    return random.choice(fallback[role])


#HYBRID EVALUATION
def evaluate_answer(question, answer):
    if USE_AI:
        try:
            prompt = f"""
Question: {question}
Answer: {answer}

Give:
1. Score (out of 100)
2. Strengths
3. Weaknesses
4. Better Answer
"""

            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[{"role": "user", "content": prompt}]
            )

            return response.choices[0].message.content
        except:
            pass  # fallback

    # fallback scoring
    words = len(answer.split())
    score = min(words * 2, 100)

    return f"""
Score: {score}/100

Strength:
You attempted the question.

Weakness:
Answer lacks depth and examples.

Better Answer:
Try explaining concept clearly with real-world examples.
"""
#NEW QUE.
if st.button("New Question") or st.session_state.question is None:
    with st.spinner("Generating question..."):
        q_text = generate_question(role, difficulty)
        st.session_state.question = q_text
        st.session_state.start_time = time.time()

# DISPLAY QUE.
if st.session_state.question:
    st.subheader("📌 Question")
    st.info(st.session_state.question)

    time_taken = int(time.time() - st.session_state.start_time)
    st.write(f"⏱ Time: {time_taken} sec")

    answer = st.text_area("✍️ Your Answer")

   
#EVALUATE
    
    if st.button("Evaluate"):
        if answer.strip() == "":
            st.warning("Write answer first")
        else:
            with st.spinner("Analyzing..."):
                feedback = evaluate_answer(st.session_state.question, answer)

            st.subheader("Feedback")
            st.write(feedback)

            score = min(len(answer.split()) * 2, 100)
            st.session_state.history.append(score)

#PERFORMANCE
st.subheader("Performance")

if st.session_state.history:
    df = pd.DataFrame(st.session_state.history, columns=["Score"])
    st.line_chart(df)
else:
    st.write("No attempts yet")
