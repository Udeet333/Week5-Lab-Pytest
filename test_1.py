import pytest
from even import is_even

@pytest.mark.parametrize("n,expected", [
    (2, True),      # positive even
    (10, True),     # positive even
    (3, False),     # positive odd
    (17, False),    # positive odd
    (0, True),      # zero is even
    (-2, True),     # negative even
    (-7, False),    # negative odd
])
def test_is_even(n, expected):
    assert is_even(n) is expected
