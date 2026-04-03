# ==============================
# 🚀 GITHUB PROJECT SETUP
# ==============================

## 📌 Repo Name
ai-interview-analyzer

## 🧾 Description
AI-powered mock interview platform with question generation, answer evaluation, and performance tracking using Streamlit.

---

## 📝 Commit Title
🚀 Initial Commit: AI Interview Analyzer (Streamlit + AI Evaluation + Auth System)

## 💬 Commit Message
Built an AI-powered interview practice platform using Streamlit with login/signup, hybrid AI question generation, answer evaluation, and performance tracking.

## 📄 Extended Description
This project is a Streamlit-based AI Interview Analyzer designed to help users practice mock interviews with real-time feedback.

Features:
- User authentication (Login/Signup using JSON)
- Role-based questions (Python Developer, Data Analyst)
- Difficulty levels (Easy, Medium, Hard)
- AI-powered evaluation (if API available)
- Fallback system without API
- Performance tracking with charts

Tech Stack:
- Python
- Streamlit
- Pandas
- OpenAI API (Optional)
- JSON

---

# ==============================
# 📘 README.md
# ==============================

# 🚀 AI Interview Analyzer

An AI-powered mock interview platform built with Streamlit that helps users practice interviews, get instant feedback, and track performance.

---

## 📌 Features

### 🔐 Authentication System
- User Signup & Login
- Session management using Streamlit
- Local storage using JSON (users.json)

---

### 🎯 Interview Practice
- Role-based questions:
  - Python Developer  
  - Data Analyst  
- Difficulty levels:
  - Easy  
  - Medium  
  - Hard  

---

### 🧠 AI-Powered Evaluation (Hybrid)
- Uses OpenAI API (if API key is provided)  
- Provides:
  - Score (out of 100)  
  - Strengths  
  - Weaknesses  
  - Improved Answer  

- Fallback system:
  - Works even without API
  - Basic evaluation based on answer length

---

### 📊 Performance Tracking
- Stores scores during session  
- Displays performance graph using Streamlit chart  

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- OpenAI API (Optional)
- JSON (Database)

---

## 📂 Project Structure

AI-Interview-Analyzer
│── interview_app.py
│── users.json
│── README.md

---

## ▶️ How to Run

1. Clone the Repository
git clone https://github.com/your-username/ai-interview-analyzer.git
cd ai-interview-analyzer

2. Install Dependencies
pip install streamlit pandas openai

3. Add OpenAI API Key (Optional)
Replace in code:
client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

4. Run the App
streamlit run interview_app.py

---

## 💡 Highlights

- Works with or without OpenAI API
- Clean UI
- Real-time interview practice
- Beginner-friendly
- Great for resume

---

## 🔮 Future Improvements

- Voice-based interview
- Database (MongoDB/MySQL)
- More roles
- PDF reports
- Timer-based tests

---

## 👨‍💻 Author

Mohd Zaid  
B.Tech CSE | Aspiring Data Analyst  

---

⭐ Star this repo if you like it!
