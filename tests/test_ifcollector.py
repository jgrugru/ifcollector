from pytest import mark
from re import search

from ifcollector import (ifandstatement,
                         iforstatement)


def matches_email_regex(value):
    match_object = search(r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$',
                          value)
    return bool(match_object)


is_valid_test_str = [
    str.isalnum,
    "len(value) > 5",
    "value == 'Testing'",
    lambda value: value == 'Testing',
]

is_valid_gmail = [
    "len(value) > 5",
    "'@' in value",
    matches_email_regex,
    "'gmail.com' in value",
    lambda value: bool(search(r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$',
                              value))
]


@mark.parametrize("value, ifstatement, expression_list, expected_result", [
    ("Test String", ifandstatement, is_valid_test_str, False),
    ("Test ", ifandstatement, is_valid_test_str, False),
    ("Testing", ifandstatement, is_valid_test_str, True),
    ("Testing1", ifandstatement, is_valid_test_str, False),
    ("Test String", iforstatement, is_valid_test_str, True),
    ("Test ", iforstatement, is_valid_test_str, False),
    ("Testing", iforstatement, is_valid_test_str, True),
    ("Testing1", iforstatement, is_valid_test_str, True),
    ("jeff.gruenbaum@gmail.com", ifandstatement, is_valid_gmail, True),
    ("jeff.gruenbaum@yahoo.com", ifandstatement, is_valid_gmail, False),
    ("@gmail.com", ifandstatement, is_valid_gmail, False),
    (" @gmail.com", ifandstatement, is_valid_gmail, False),
])
def test_ifstatements(value, ifstatement, expression_list, expected_result):
    assert ifstatement(value,
                       *expression_list,
                       debug=True) == expected_result
