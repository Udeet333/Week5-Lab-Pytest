import pytest
from strings import reverse_string

@pytest.mark.parametrize("s,expected", [
    ("hello", "olleh"),
    ("", ""),
    ("a", "a"),
    ("RaceCar", "raCecaR"),
    ("12345", "54321"),
    ("!@#", "#@!"),
])
def test_reverse_string(s, expected):
    assert reverse_string(s) == expected
