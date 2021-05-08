from pytest import mark
from re import search

from ifcollector.if_functions import (ifandstatement,
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
    "'gmail.com' in value"
]


@mark.parametrize("value, expression_list, expected_result", [
    ("Test String", is_valid_test_str, False),
    ("Test ", is_valid_test_str, False),
    ("Testing", is_valid_test_str, True),
    ("Testing1", is_valid_test_str, False),
])
def test_ifandstatement(value, expression_list, expected_result):
    assert ifandstatement(value,
                          *expression_list,
                          debug=True) == expected_result


@mark.parametrize("value, expression_list, expected_result", [
    ("Test String", is_valid_test_str, True),
    ("Test ", is_valid_test_str, False),
    ("Testing", is_valid_test_str, True),
    ("Testing1", is_valid_test_str, True),
])
def test_iforstatement(value, expression_list, expected_result):
    assert iforstatement(value,
                         *expression_list,
                         debug=True) == expected_result


@mark.parametrize("value, expression_list, expected_result", [
    ("jeff.gruenbaum@gmail.com", is_valid_gmail, True),
    ("jeff.gruenbaum@yahoo.com", is_valid_gmail, False),
    ("@gmail.com", is_valid_gmail, False),
    (" @gmail.com", is_valid_gmail, False),
])
def test_email_input(value, expression_list, expected_result):
    assert ifandstatement(value,
                          *expression_list,
                          debug=True) == expected_result
