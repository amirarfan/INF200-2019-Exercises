# -*- coding: utf-8 -*-

__author__ = "Amir Arfan"
__email__ = "amar@nmbu.no"


# Median code obtained by Yngve from lecture 04


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """

    sorted_data = sorted(data)
    num_elements = len(sorted_data)
    if num_elements % 2 == 1:
        return sorted_data[num_elements // 2]
    elif num_elements == 0:
        raise ValueError
    else:
        return (
            (sorted_data[(num_elements // 2) - 1] + sorted_data[
            num_elements // 2]) / 2
        )


def test_median_of_single_element():
    assert median([5]) == 5


def test_median_of_different_inputs():
    odd_data = [4, 6, 7, 5, 9]
    assert median(odd_data) == 6

    even_data = [4, 6, 7, 9]
    assert median(even_data) == 6.5

    ordered_data = [4, 5, 6, 7, 9]
    assert median(ordered_data) == 6

    reverse_ordered_data = [9, 7, 6, 5, 4]
    assert median(reverse_ordered_data) == 6

    unordered_data = [3, 2, 4, 1, 5]
    assert median(unordered_data) == 3


def test_median_raises_value_error_on_empty_list():
    try:
        median([])
    except ValueError:
        pass
    else:
        assert False


