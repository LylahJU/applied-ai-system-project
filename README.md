# 🎮 AI Game Glitch Investigator

## 📌 Original Project - Game Glitch Investigator
This project began as a Streamlit-based number guessing game where users try to guess a secret number with hints and scoring.

## 🤖 AI Feature: Agentic Hint System
This version introduces an AI agent that:
- Analyzes guess history
- Plans better strategies
- Generates hints
- Outputs confidence scores

## 🏗️ System Architecture
User Input → Validation → Game Logic → History → AI Agent (analyze → plan → hint → confidence) → UI Output → Logging & Tests

💬 Sample Interactions

**Input**: 25
**Output**: Too Low
**AI Hint**: Try a higher number closer to midpoint
**Confidence**: 0.7

🧪 Testing Summary
- All logic tests pass
- AI tests pass
- Confidence increases with more guesses

🧠 Design Decisions
- Used agentic AI instead of RAG for simplicity
- Added confidence scoring for reliability
- Integrated AI directly into gameplay

⚖️ Ethics & Limitations
- AI does not know the correct answer
- May give suboptimal hints early
- Confidence may not reflect true accuracy

## ⚙️ Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`