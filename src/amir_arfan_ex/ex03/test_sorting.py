# -*- coding: utf-8 -*-

__author__ = "Amir Arfan"
__email__ = "amar@nmbu.no"


def bubble_sort(data_to_be_sorted):
    """
    Sort data using the bubble sort method,
    returns the sorted data as a new list.

    """
    n_length = len(data_to_be_sorted)
    sorted_data = list(data_to_be_sorted)
    # Transforms the data to be sorted into a new list
    for i in range(n_length):
        for j in range(n_length - i - 1):
            if sorted_data[j] > sorted_data[j + 1]:
                # Using the bubble sort method, checking if current
                # iteration is greater than the next iteration, if it is,
                # they are swapped. Possible to do this with while loop
                sorted_data[j], sorted_data[j + 1] = (
                    sorted_data[j + 1],
                    sorted_data[j],
                )
    return sorted_data


def test_empty():
    """Test that the sorting function works for empty list"""
    assert bubble_sort([]) == []


def test_single():
    """Test that the sorting function works for single-element list"""
    assert bubble_sort([1]) == [1]
    assert len(bubble_sort([1])) == 1


def test_sorted_is_not_original():
    """
    Test that the sorting function returns a new object.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert data != sorted_data


def test_original_unchanged():
    """
    Test that sorting leaves the original data unchanged.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now data shall still contain [3, 2, 1].
    """
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert data == [3, 2, 1]
    assert sorted_data != data


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    data = [1, 2, 3]
    sorted_data = bubble_sort(data)
    for small, large in zip(sorted_data[:-1], sorted_data[1:]):
        assert small < large


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    for small, large in zip(sorted_data[:-1], sorted_data[1:]):
        assert small < large


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    data = [1, 1, 1]
    sorted_data = bubble_sort(data)
    for previous, after in zip(sorted_data[:-1], sorted_data[1:]):
        assert previous == after


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """

    # Test if the sorting function works for float
    float_data = [2.9, 5.4, 10.7, 9.9]
    sorted_float_data = bubble_sort(float_data)
    for small, large in zip(sorted_float_data[:-1], sorted_float_data[1:]):
        assert small < large

    # Test if the sorting functions work for sorting strings alphabetically
    list_of_strings = ["hello", "goodbye", "albert"]
    sorted_string_data = bubble_sort(list_of_strings)
    for small, large in zip(sorted_string_data[:-1], sorted_string_data[1:]):
        assert small < large

    # Test if bubble_sort gives equivalent output as sort function integrated
    # Python

    data = [2, 6, 7, 1, 4]
    sorted_by_bubblesort = bubble_sort(data)
    sorted_by_python = sorted(data)
    for bubble, python in zip(sorted_by_bubblesort, sorted_by_python):
        assert bubble == python

    # Testing if bubble_sort gives equivalent output with try except and assert
    for bubble, python in zip(sorted_by_bubblesort, sorted_by_python):
        try:
            assert bubble != python
        except AssertionError:
            print("Element is equivalent")
