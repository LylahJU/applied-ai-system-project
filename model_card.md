
# 🎮 Model Card: AI Game Glitch Investigator

## 1) What is this system?
AI-enhanced guessing game with an agentic hint generator.

## 2) How it works
Input → analyze → AI generates hint → confidence output

## 3) Inputs/Outputs
Inputs: guesses  
Outputs: hints, confidence  

## 4) Reliability Rules
- Input validation
- Confidence scoring
- Logging

## 5) Failure Modes
- Weak early hints
- Misleading patterns

## 6) AI vs Logic
Logic is correct but simple  
AI is adaptive but imperfect  

## 7) Human-in-the-loop
Low confidence should trigger user caution

## 8) Improvement
Add retrieval-based strategies (RAG)