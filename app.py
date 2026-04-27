import random
import streamlit as st
import logging

from logic_utils import parse_guess, check_guess, get_range_for_difficulty, update_score
from ai_agent import generate_ai_hint

# Setup logging
logging.basicConfig(filename="game.log", level=logging.INFO)

st.set_page_config(page_title="AI Glitchy Guesser", page_icon="🎮")

st.title("🎮 AI Game Glitch Investigator")
st.caption("Now powered by an AI Coach 🤖")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 8,
    "Normal": 6,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

# Session state initialization
if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

st.subheader("Make a guess")

st.info(
    f"Guess a number between {low} and {high}. "
    f"Attempt {st.session_state.attempts + 1} of {attempt_limit}"
)

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("History:", st.session_state.history)

raw_guess = st.text_input("Enter your guess:")

col1, col2 = st.columns(2)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")

# New game reset
if new_game:
    st.session_state.secret = random.randint(low, high)
    st.session_state.attempts = 0
    st.session_state.score = 0
    st.session_state.history = []
    st.session_state.status = "playing"
    st.success("New game started.")
    st.rerun()

# Stop if game finished
if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game.")
    else:
        st.error("Game over. Start a new game.")
    st.stop()

# Handle guess
if submit:
    ok, guess_int, err = parse_guess(raw_guess, low, high)

    if not ok:
        st.error(err)
        logging.warning(f"Invalid input: {raw_guess}")
        st.stop()
    else:
        st.session_state.attempts += 1

    if not ok:
        st.error(err)
        logging.warning(f"Invalid input: {raw_guess}")
    else:
        # First: check guess to get outcome
        outcome, message = check_guess(guess_int, st.session_state.secret)

        # Then: store BOTH guess and outcome
        st.session_state.history.append((guess_int, outcome))

        # Show feedback
        st.warning(message)

        # Update score
        st.session_state.score = update_score(
            st.session_state.score,
            outcome,
            st.session_state.attempts
        )

        # AI Agent Hint (now uses correct structured history)
        ai_output = generate_ai_hint(
            st.session_state.history,
            low,
            high
        )

        st.info(f"🤖 AI Coach: {ai_output['hint']}")
        st.caption(f"Confidence: {ai_output['confidence']}")

        logging.info(f"AI Hint: {ai_output}")

        if outcome == "Win":
            st.balloons()
            st.session_state.status = "won"
            st.success(f"You won! Score: {st.session_state.score}")

        elif st.session_state.attempts >= attempt_limit:
            st.session_state.status = "lost"
            st.error(f"Out of attempts! Secret was {st.session_state.secret}")

st.divider()
st.caption("AI-powered guessing game with agentic hints and reliability tracking.")