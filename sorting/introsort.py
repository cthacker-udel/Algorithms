from helpers.generate_array import generate_array
from quicksort import thacker_quicksort
from typing import List


def introsort(arr: List[int], insertionThreshold: int = 16, recursionLimit=5, recursionDepth: int = 0) -> List[int]:
    """
    Comparison based sorting algorithm, which utilizes other sorting algorithms to achieve peak efficiency

    Args:
        arr (List[int]): The list of numbers to sort
        insertionThreshold (int, optional): The # of elements in the array we test the threshold against to determine whether we need to run insertion sort on the array. Defaults to 16.
        recursionLimit (int, optional): The limit of recursion we require to utilize heapsort on the array. Defaults to 5.
        recursionDepth (int, optional): The current depth of recursion in the call-stack. Defaults to 0.

    Returns:
        List[int]: The sorted list of elements
    """
    if len(arr) < insertionThreshold:
        return insertion_sort(arr)
    elif recursionDepth > recursionLimit:
        return heap_sort(arr)
    else:
        pivot = len(arr) // 2
        introsort(arr[:pivot], insertionThreshold,
                  recursionLimit, recursionDepth + 1)
        introsort(arr[pivot:], insertionThreshold,
                  recursionLimit, recursionDepth + 1)
        return arr
