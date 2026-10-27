def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 50


def parse_guess(raw, low=1, high=100):
    if raw is None or str(raw).strip() == "":
        return False, None, "Enter a guess."

    raw = str(raw).strip()
    try:
        value = int(raw)
    except ValueError:
        return False, None, "Enter a whole number."

    if not low <= value <= high:
        return False, None, f"Guess must be between {low} and {high}."

    return True, value, None

def check_guess(guess, secret):
    guess = int(guess)
    secret = int(secret)

    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome == "Win":
        points = max(10, 100 - 10 * (attempt_number - 1))
        return current_score + points

    if outcome in ("Too High", "Too Low"):
        return current_score - 5

    return current_score