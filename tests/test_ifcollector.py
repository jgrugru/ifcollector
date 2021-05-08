from pytest import mark

from ifcollector.if_functions import (ifandstatement,
                                      iforstatement)


is_valid_test_str = [
    str.isalnum,
    "len(value) > 5",
    "value == 'Testing'",
    lambda value: value == 'Testing',
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
                         *is_valid_test_str,
                         debug=True) == expected_result
