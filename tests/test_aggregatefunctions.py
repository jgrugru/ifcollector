
from ifaggregate.AggregateFunctions import ifandstatement


def is_str(value):
    if isinstance(value, str):
        return True
    else:
        return False


def contains_at(value):
    if 'T' in value:
        return True
    else:
        return False


is_valid_test_str = [
    str.isalnum,
    is_str,
    contains_at,
    "value == 'IamastTring'",
]


def test_ifandstatement():
    assert ifandstatement("IamastTring", *is_valid_test_str, debug=True)
