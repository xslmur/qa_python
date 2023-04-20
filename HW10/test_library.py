import pytest
import library


testcases_remove_lowercase_positive = [
    ('длоОЛО  55 !', 'ОЛО'),
    ('abc', ''),
    ('ABC', 'ABC'),
    ('', ''),
    ('X' * 50, 'X' * 25),
    ('Qw' * 100, 'Q' * 25)
]


@pytest.mark.parametrize('input_str, expected', testcases_remove_lowercase_positive)
def test_remove_lowercase_positive(input_str, expected):
    assert library.remove_lowercase(input_str) == expected, 'something went wrong'


