def get_range_for_difficulty(difficulty: str):
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 100


def parse_guess(raw: str, low: int = 1, high: int = 100):
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except:
        return False, None, "That is not a number."

    if value < low or value > high:
        return False, None, f"Please enter a number between {low} and {high}."

    return True, value, None


def check_guess(guess, secret):
    if guess == secret:
        return "Win", "🎉 Correct!"
    elif guess > secret:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome == "Win":
        points = max(10, 100 - 10 * attempt_number)
        return current_score + points
    elif outcome == "Too High":
        return current_score + 5 if attempt_number % 2 == 0 else current_score - 5
    elif outcome == "Too Low":
        return current_score - 5
    return current_score