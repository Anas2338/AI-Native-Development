# Study Notes Summarizer & Quiz Generator Agent

## project overview
A sleek, intelligent web application that transforms any uploaded PDF into clean, revision-ready study notes and generates high-quality, text-faithful quizzes — perfect for students, researchers, and lifelong learners.

## Core Features
- Drag & drop PDF upload
- Accurate text extraction with pypdf
- Three gorgeous summary styles (user selects):
  - Bullet Notes
  - Blocks (clean sections)
  - Flashcards (ready for Anki)
- Smart quiz generation (MCQs + explanations) using dedicated agents
- All content 100% grounded in the original PDF — zero hallucination

## Tech Stack
- **Language**: Python 3.11+
- **UI**: Streamlit
- **Python library**: pypdf
- **SDK**: Openai-agents sdk
- **Package Manager**: UV (without src directory)

## Environment & Dependencies
- Create a `.env` template.
- List necessary packages in `pyproject.toml` (ensure `openai-agents` is included).

## Project Structure
notes_summarizer/
├── main.py                      # Main Streamlit application
│
├── core/                       # Core business logic (simple, clean)
│   ├── pdf.py                  # PDF extraction
│   ├── summarize.py            # Summaries (bullet, block, flashcards)
│   ├── quiz.py                 # Quiz generation logic (MCQs + explanations)
│
├── agents/                     # OpenAI Agents layer
│   ├── summarize_agent.py      # Summarizer agent
│   ├── quiz_agent.py           # Quiz generator agent
│
├── tests/                      # Lightweight testing structure
│   ├── test_pdf.py
│   ├── test_summarize.py
│   ├── test_quiz.py
│   └── test_agents.py
│
├── .env                # Environment variables template
├── .gitignore
├── gemini.md
└── pyproject.toml