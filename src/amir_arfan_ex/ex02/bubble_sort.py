def bubble_sort(data_to_be_sorted):
    """
    Sort data using the bubble sort method, returns the sorted data as a new list.

    """
    n_length = len(data_to_be_sorted)
    sorted_data = list(data_to_be_sorted)  # Transforms the data to be sorted into a new list
    for i in range(n_length):
        for j in range(n_length - i - 1):
            if sorted_data[j] > sorted_data[j + 1]:  # Using the bubble sort method, checking if current iteration
                # is greater than the next iteration, if it is, they are swapped. Possible to do this with while loop
                sorted_data[j], sorted_data[j + 1] = sorted_data[j + 1], sorted_data[j]
    return sorted_data


if __name__ == "__main__":

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
