from typing import List
from random import choice, randint
from helpers.generate_array import generate_array


def thacker_quicksort(numbers: List[int]) -> List[int]:
    """
    Homemade quicksort, with no additional help with choosing the pivot
    Not Stable
    In place
    Divide and Conquer Algorithm
    Best O(n lg n)
    Worst O(n^2)

    Args:
        numbers (List[int]): The list of numbers that we will be sorting
        pivot (int, optional): The pivot we chose. Defaults to 0.
    """
    if len(numbers) <= 2:
        return numbers if len(numbers) <= 1 else [min(numbers[0], numbers[1]), max(numbers[0], numbers[1])]
    # choose the index of the pivot (randomly generating an index)
    pivot_ind = randint(0, len(numbers) - 1)
    # grab and set the value we are pivoting on
    pivot_value = numbers[pivot_ind]
    # formulate two sub-arrays
    less_than = []
    greater_than = []
    for ind, element in enumerate(numbers):
        if numbers[ind] < pivot_value:
            less_than.append(numbers[ind])
        elif ind != pivot_ind:
            greater_than.append(numbers[ind])
    numbers[pivot_ind + 1:] = thacker_quicksort(greater_than)
    numbers[:pivot_ind] = thacker_quicksort(less_than)
    return numbers


def lomuto_quicksort(numbers: List[int], lo: int = 0, hi: int = 0) -> List[int]:
    """
    The lomuto partition scheme for quicksort, it chooses the last element in the array as the pivot, and maintains an index i as it scans the array using another index j
    such that elements at lo through i - 1 are less than the pivot, and elements i through j are equal to or greater then the pivot.
    This sorts partitions of an array

    Args:
        numbers (List[int]): The list of numbers to sort
        lo (int, optional): The lower part of the sub-array. Defaults to 0.

    Returns:
        List[int]: The sorted list of numbers
    """
    if len(numbers) <= 1:
        return numbers
    elif len(numbers) == 2:
        return [min(numbers), max(numbers)]
    pivot = max(numbers[lo:hi + 1])
    lesser = []
    greater = []
    for i in range(lo, hi):
        for j in range(i, hi):
            if numbers[j] < pivot:
                lesser.append(numbers[i])
            else:
                greater.append(numbers[i])
        numbers[lo:i] = lomuto_quicksort(lesser, 0, len(lesser) - 1)
        numbers[i:j + 1] = lomuto_quicksort(greater, 0, len(greater) - 1)
    return numbers


for i in range(10):
    arr = generate_array(10, 1, 200)
    print(thacker_quicksort(arr) == sorted(arr))
    print(lomuto_quicksort(arr, 0, len(arr)))
