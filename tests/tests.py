import pytest

from main import sum_numbers


def test_wrong_indexing_error():
    my_list = ['dog', 'cat', 5, 'parrot', 0, 'O']
    with pytest.raises(expected_exception=TypeError):
        my_list[3.0]


@pytest.mark.parametrize("a, b , c, expected_result", [(1, 2, 6, 9), (5, 10, 15, 30), (1, 1, -2, 0), (10, -5, -7, -2)])
def test_sum_numbers(a, b, c, expected_result):
    assert sum_numbers(a, b, c) == expected_result


def test_insert_method():
    my_list = ['poetry', 'space', 42, 'tea']
    my_list.insert(2, 'coffee')
    assert my_list == ['poetry', 'space', 'coffee', 42, 'tea']


def test_extend_list_method():
    my_list = ['dog', 'cat', 'whale']
    definitely_not_my_list = ['parrot', 'sparrow', 'eagle', 'hawk']
    my_list.extend(definitely_not_my_list)
    assert my_list == ['dog', 'cat', 'whale', 'parrot', 'sparrow', 'eagle', 'hawk']


def test_str_to_int():
    a = '12'
    a = int(a)
    assert type(a) == int


def test_integer_type_error():
    a = 2
    with pytest.raises(expected_exception=TypeError):
        a += 'dog'


@pytest.mark.parametrize("from_sys,to_base , expected_result", [('0b110', 2, 6), ('0o11', 8, 9), ('0xf', 16, 15)])
def test_conversion_to_another_numeral_system(from_sys, to_base, expected_result):
    assert int(from_sys, base=to_base) == expected_result
