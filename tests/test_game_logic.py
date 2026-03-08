from logic_utils import check_guess, parse_guess

# --- check_guess tests ---
# Bug: hints were displaying incorrectly
def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_high_low_messages():
    # If guess is too high, message should say to go lower
    _, message_high = check_guess(60, 50)
    assert "LOWER" in message_high

    # If guess is too low, message should say to go higher
    _, message_low = check_guess(40, 50)
    assert "HIGHER" in message_low

# --- parse_guess tests ---
# Bug: invalid guesses were being added to history without proper validation
def test_parse_empty_string():
    ok, val, err = parse_guess("")
    assert ok == False
    assert val is None

def test_parse_none():
    ok, val, err = parse_guess(None)
    assert ok == False

def test_parse_non_number():
    ok, val, err = parse_guess("abc")
    assert ok == False
    assert "not a number" in err.lower()

def test_parse_valid_number():
    ok, val, err = parse_guess("42")
    assert ok == True
    assert val == 42
    assert err is None