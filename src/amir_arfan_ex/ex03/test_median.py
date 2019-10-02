# -*- coding: utf-8 -*-

__author__ = "Amir Arfan"
__email__ = "amar@nmbu.no"


# Median code obtained by Yngve from lecture 04
# Updated by me to work properly.


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """

    sorted_data = sorted(data)
    num_elements = len(sorted_data)
    if num_elements % 2 == 1:  # Using DivMod to check if list is odd
        return sorted_data[num_elements // 2]
    elif num_elements == 0:
        raise ValueError  # Raises ValueError if list is empty
    else:
        return (
            sorted_data[(num_elements // 2) - 1]
            + sorted_data[num_elements // 2]
        ) / 2


def test_median_of_single_element():
    """
    Testing if the median function works for a single element list

    """
    assert median([5]) == 5


def test_median_of_different_inputs():
    """

    Testing the median with different kinds of input, for an odd list,
    even list, ordered list, reverse ordered list, and non-sorted data.

    """
    odd_data = [4, 6, 7, 5, 9]  # Initializing an odd list
    assert median(odd_data) == 6

    even_data = [4, 6, 7, 9]  # Initializing an even list
    assert median(even_data) == 6.5

    ordered_data = [4, 5, 6, 7, 9]  # Initializing a list with ordered data
    assert median(ordered_data) == 6

    reverse_ordered_data = [
        9,
        7,
        6,
        5,
        4,
    ]  # Initializing a reverse sorted list
    assert median(reverse_ordered_data) == 6

    unordered_data = [3, 2, 4, 1, 5]  # Initializing a non - sorted list
    assert median(unordered_data) == 3


def test_median_raises_value_error_on_empty_list():
    """
    Test if the median function raises a value error if the input is an empty
    list

    """
    try:
        median([])
    except ValueError:
        pass
    else:
        assert False
    # Using try, except, else statements to create a test.


def test_median_is_not_original():
    """
    Test if the median function does not alter the original data

    """
    data = [3, 2, 4, 1, 5]
    median_data = median(data)
    assert median_data == 3  # Added to check if median is calculated as well
    assert data == data  # as the list is not changed


def test_median_tuple():
    """
    Test if the median function works for tuple input.
    """
    tuple_data = {1, 2, 4, 3, 5}
    assert median(tuple_data) == 3
