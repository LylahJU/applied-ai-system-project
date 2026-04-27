import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from logic_utils import check_guess, parse_guess

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

# Tests for parse_guess function
def test_parse_guess_valid_integer():
    # Test that a valid integer within the range is parsed correctly
    ok, value, err = parse_guess("10", 1, 20)
    assert ok == True
    assert value == 10
    assert err is None

def test_parse_guess_decimal():
    # Test that decimal inputs are converted to integers
    ok, value, err = parse_guess("5.7", 1, 20)
    assert ok == True
    assert value == 5
    assert err is None

def test_parse_guess_characters():
    # Test that non-numeric characters are rejected
    ok, value, err = parse_guess("abc", 1, 20)
    assert ok == False
    assert value is None
    assert err == "That is not a number."

def test_parse_guess_too_large():
    # Test that numbers above the maximum range are rejected
    ok, value, err = parse_guess("25", 1, 20)
    assert ok == False
    assert value is None
    assert err == "Please enter a number between 1 and 20."

def test_parse_guess_too_small():
    # Test that numbers below the minimum range are rejected
    ok, value, err = parse_guess("0", 1, 20)
    assert ok == False
    assert value is None
    assert err == "Please enter a number between 1 and 20."

def test_parse_guess_too_large_normal():
    # Test that numbers too large for Normal difficulty are rejected
    ok, value, err = parse_guess("60", 1, 50)
    assert ok == False
    assert value is None
    assert err == "Please enter a number between 1 and 50."

def test_parse_guess_too_large_hard():
    # Test that numbers too large for Hard difficulty are rejected
    ok, value, err = parse_guess("150", 1, 100)
    assert ok == False
    assert value is None
    assert err == "Please enter a number between 1 and 100."

def test_parse_guess_empty_string():
    # Test that empty string inputs are rejected
    ok, value, err = parse_guess("", 1, 20)
    assert ok == False
    assert value is None
    assert err == "Enter a guess."

def test_parse_guess_none():
    # Test that None inputs are rejected
    ok, value, err = parse_guess(None, 1, 20)
    assert ok == False
    assert value is None
    assert err == "Enter a guess."