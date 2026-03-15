def get_range_for_difficulty(difficulty: str):
    """
    Return (low, high) inclusive range for a given difficulty.

    Args:
        difficulty (str): The difficulty level, one of "Easy", "Normal", or "Hard".

    Returns:
        tuple[int, int]: A tuple containing the lower and upper bounds of the range.
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Handles empty strings, non-numeric input, and floats by truncating.

    Args:
        raw (str): The raw string input from the user.

    Returns:
        tuple[bool, int | None, str | None]: A tuple containing:
            - bool: True if parsing was successful, False otherwise.
            - int | None: The parsed integer if successful, otherwise None.
            - str | None: An error message if parsing failed, otherwise None.
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess: int, secret: int):
    """
    Compare guess to secret and return an outcome and a message.

    Args:
        guess (int): The user's guess.
        secret (int): The secret number.

    Returns:
        tuple[str, str]: A tuple containing:
            - str: The outcome of the guess ("Win", "Too High", "Too Low").
            - str: A message to display to the user.
    """
    if guess == secret:
        return "Win", "🎉 Correct!"
    elif guess > secret:
        return "Too High", "📈 Go LOWER!"
    else:
        return "Too Low", "📉 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """
    Update score based on the outcome of the guess and the attempt number.

    Args:
        current_score (int): The player's current score.
        outcome (str): The outcome of the guess ("Win", "Too High", "Too Low").
        attempt_number (int): The current attempt number.

    Returns:
        int: The updated score.
    """
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
