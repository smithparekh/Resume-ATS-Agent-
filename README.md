# Resume ATS Agent

> Multi-agent AI system that rewrites and scores your resume for Applicant Tracking Systems (ATS)

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![CrewAI](https://img.shields.io/badge/CrewAI-FF6B6B?style=flat&logoColor=white)](https://crewai.com)
[![OpenAI](https://img.shields.io/badge/GPT--4o--mini-412991?style=flat&logo=openai&logoColor=white)](https://openai.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io)

---

## What It Does

Paste your resume and a job description. Four specialized AI agents collaborate to:

1. **Parser Agent** — Extracts skills, experience, and keywords from your resume
2. **ATS Writer Agent** — Rewrites your resume bullets to match the job description
3. **Refiner Agent** — Polishes language, removes fluff, sharpens impact
4. **Evaluator Agent** — Scores the final resume and highlights remaining gaps

The result is a download-ready, ATS-optimized resume tailored to the specific job.

---

## Architecture

```
Resume + Job Description
        |
        v
  [Parser Agent]  ──── extracts skills, keywords, experience
        |
        v
  [ATS Writer Agent]  ──── rewrites bullets to match JD keywords
        |
        v
  [Refiner Agent]  ──── cleans language, improves impact statements
        |
        v
  [Evaluator Agent]  ──── scores ATS match, flags missing keywords
        |
        v
  Streamlit UI  ──── shows rewritten resume + score + download (.txt / .docx)
```

---

## Tech Stack

| Component | Technology |
|---|---|
| Agent Orchestration | CrewAI |
| LLM | OpenAI GPT-4o-mini |
| Frontend | Streamlit |
| Output | Plain text + DOCX download |

---

## Setup

```bash
git clone https://github.com/smithparekh/Resume-ATS-Agent-
cd Resume-ATS-Agent-
pip install -r requirements.txt

# Add your OpenAI API key
export OPENAI_API_KEY=your_key_here

streamlit run streamlit_app.py
```

---

## Key Features

- 4-agent sequential pipeline built with CrewAI
- Real-time streaming output in Streamlit UI
- Download optimized resume as .txt or .docx
- Configurable GPT-4o-mini model via sidebar
