import logging

logging.basicConfig(filename="game.log", level=logging.INFO)

def generate_ai_hint(history, low, high):
    """
    Agentic hint system:
    - Tracks valid range based on past guesses
    - Shrinks search space
    - Suggests optimal next guess (binary search)
    """

    # Initial range
    min_val = low
    max_val = high

    # No history → start at midpoint
    if not history:
        midpoint = (low + high) // 2
        return {
            "hint": f"Start near the middle: {midpoint}",
            "confidence": 0.6
        }

    # Update range using history
    for guess, outcome in history:
        if outcome == "Too Low":
            min_val = max(min_val, guess + 1)
        elif outcome == "Too High":
            max_val = min(max_val, guess - 1)

    # Guardrail: invalid state
    if min_val > max_val:
        logging.error("Invalid range detected from history.")
        return {
            "hint": "Something went wrong — try restarting the game.",
            "confidence": 0.2
        }

    # Optimal next guess (binary search)
    midpoint = (min_val + max_val) // 2

    hint = f"Try a number between {min_val} and {max_val}. A good guess is {midpoint}."

    # Confidence increases as range shrinks
    range_size = max_val - min_val + 1
    total_range = high - low + 1
    confidence = 1 - (range_size / total_range)

    confidence = max(0.5, round(confidence, 2))

    logging.info(f"Range: [{min_val}, {max_val}] | Hint: {hint} | Confidence: {confidence}")

    return {
        "hint": hint,
        "confidence": confidence
    }