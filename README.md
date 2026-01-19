# 📄 Resume ATS Agent

## 🧠 AI-Powered Resume Screening & Optimization System

Resume ATS Agent is an AI-driven application designed to simulate how modern Applicant Tracking Systems (ATS) evaluate resumes. It analyzes resumes against job descriptions, identifies missing skills and keywords, and generates actionable recommendations to improve shortlisting potential.

This project demonstrates the practical use of AI agents, workflow orchestration, and prompt engineering to solve a real-world recruitment problem.

---

## 🚀 Key Features

- Resume vs Job Description matching  
- AI-based skill and keyword extraction  
- ATS-style compatibility analysis  
- Personalized resume improvement suggestions  
- Streamlit-based user interface  
- Secure environment variable–based API key handling  

---

## 🏗️ Project Structure

resume_ats_agent/


├── agents.py           # AI agent definitions & logic

├── tasks.py            # Tasks and evaluation workflows

├── crew.py             # Agent orchestration layer

├── utils.py            # Utility & helper functions

├── file_tools/         # File processing utilities

├── streamlit_app.py    # Streamlit web application

├── requirements.txt   # Python dependencies

└── README.md


## ▶️ Running the Application

Streamlit Web App
streamlit run streamlit_app.py

## 🎯 Use Cases

Job seekers optimizing resumes for ATS systems

Recruiters performing fast pre-screening

Career coaches and resume consultants

AI-powered HR and recruitment tools

🔐 Security & Best Practices

API keys are managed using environment variables

Sensitive files are excluded using .gitignore

No secrets are hard-coded in the application

## 📈 Future Enhancements

Resume scoring and ranking dashboard

PDF & DOCX resume upload

Multi-job role comparison

ATS report export

Keyword coverage visualization



