import matplotlib.pyplot as plt


# we only want to use lowercase letters for function names
def assignment(new_list, i, old_list, j):
    # added docstring to explain the function
    """
    Assigns a new value to the specified index of a list
    using the given index of another list.

    Args:
        new_list: list
            List we want to change.
        i: integer
            Index of new_list we want to change.
        old_list: list
            List which has the new value.
        j: integer
            Index of the value we want to use.

    Returns:
        None, this function changes a value in-place
    """
    new_list[i] = old_list[j]


# function names using multiple words should be combined by using _
def merge_sort(list_to_sort_by_merge):
    # added docstring to explain the function
    """
    Standard (divide and conquer) implementation of in-place (!) Mergesort.

    Args:
        list_to_sort_by_merge: list (of comparable values)
            The list we want to sort by using Mergesort

    Returns:
        None, this function changes values in-place
    """
    # the other two comparisons had no effect
    # only > 1 is needed
    if len(list_to_sort_by_merge) > 1:
        # finding middle index
        mid = len(list_to_sort_by_merge) // 2
        # splitting the array at this index using slicing
        left = list_to_sort_by_merge[:mid]
        right = list_to_sort_by_merge[mid:]

        # recursive calls
        merge_sort(left)
        merge_sort(right)

        # cleared up variable names
        left_index = 0
        right_index = 0
        i = 0

        # move indices according to comparisons
        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                # lines should be 79 characters long at most
                assignment(list_to_sort_by_merge, i, left, left_index)
                left_index += 1
            else:
                # lines should be 79 characters long at most
                assignment(list_to_sort_by_merge, i, right, right_index)
                right_index += 1
            i += 1

        # swap values
        while left_index < len(left):
            list_to_sort_by_merge[i] = left[left_index]
            left_index += 1
            i += 1

        while right_index < len(right):
            list_to_sort_by_merge[i] = right[right_index]
            right_index += 1
            i += 1


# plotting
my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# range object does not change by plotting
# therefore we only need to initialize x once
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
merge_sort(my_list)
plt.plot(x, my_list)
plt.show()
