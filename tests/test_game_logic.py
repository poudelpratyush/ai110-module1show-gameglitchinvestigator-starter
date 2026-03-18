import pytest

from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


@pytest.mark.parametrize(
    "difficulty,expected",
    [
        ("Easy", (1, 20)),
        ("Normal", (1, 100)),
        ("Hard", (1, 50)),
    ],
)
def test_difficulty_sets_expected_range(difficulty, expected):
    """Regression test: selected difficulty must drive the guess range."""
    assert get_range_for_difficulty(difficulty) == expected


def test_unknown_difficulty_falls_back_to_normal_range():
    assert get_range_for_difficulty("Impossible") == (1, 100)


def test_parse_guess_trims_and_accepts_integer_strings():
    ok, value, err = parse_guess(" 42 ")
    assert ok is True
    assert value == 42
    assert err is None


def test_parse_guess_rejects_empty_input():
    ok, value, err = parse_guess("   ")
    assert ok is False
    assert value is None
    assert err == "Enter a guess."


def test_update_score_win_is_clamped_to_minimum_points():
    # Late wins still award at least 10 points.
    assert update_score(current_score=0, outcome="Win", attempt_number=30) == 10
