import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_multiple_streaks():
    """Test that the function returns the length of the longest streak."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_with_zeros_and_negatives():
    """Test that zeros and negative numbers correctly break streaks."""
    assert longest_positive_streak([1, 2, 0, 3, -4, 5, 6, 7, 8]) == 4

def test_all_positive_numbers():
    """Test a list containing only positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_all_non_positive_numbers():
    """Test a list with no positive numbers."""
    assert longest_positive_streak([-1, -2, 0, -5]) == 0

def test_streak_at_the_beginning():
    """Test a list where the longest streak is at the beginning."""
    assert longest_positive_streak([5, 6, 7, -1, 2, 3]) == 3

def test_streak_at_the_end():
    """Test a list where the longest streak is at the end."""
    assert longest_positive_streak([1, 2, -1, 4, 5, 6, 7]) == 4

def test_single_positive_element():
    """Test a list with a single positive number."""
    assert longest_positive_streak([10]) == 1

def test_single_non_positive_element():
    """Test a list with a single non-positive number."""
    assert longest_positive_streak([-10]) == 0

def test_no_streak():
    """Test a list with alternating positive and non-positive numbers."""
    assert longest_positive_streak([1, -1, 2, -2, 3, -3]) == 1