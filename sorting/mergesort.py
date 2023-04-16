from typing import List
from helpers.generate_array import generate_array
import timeit
import matplotlib.pyplot as plt


def merge_sort(array: List[int]) -> List[int]:
    """
    Comparison based sorting algorithm
    Mostly stable (meaning order of elements is kept)
    Divide and conquer

    Args:
        array (List[int]): The list to sort

    Returns:
        List[int]: The sorted list
    """
    if len(array) == 1:
        return array[0]
    else:
        spl = len(array) // 2
        n_left = array[:spl]
        n_right = array[spl:]
        merge_sort(n_left)
        merge_sort(n_right)
        sorted_arr = []
        i, j, placer = 0, 0, 0
        while i < len(n_left) or j < len(n_right):
            if i < len(n_left):
                if j < len(n_right) and n_right[j] < n_left[i]:
                    sorted_arr.append(n_right[j])
                    j += 1
                else:
                    sorted_arr.append(n_left[i])
                    i += 1
            elif j < len(n_right):
                sorted_arr.append(n_right[j])
                j += 1
        array[:] = sorted_arr


if __name__ == '__main__':
    lens = [10**1, 10**2, 10**3, 10**4, 10**5, 10**6, 10**7, 10**8]
    times = []
    plt.xlabel("Time")
    plt.ylabel("# of elements")
    for each_arr_len in lens:
        arr = generate_array(each_arr_len, 1, 1000)
        arr_copy = arr[:]
        start = timeit.default_timer()
        merge_sort(arr_copy)
        stop = timeit.default_timer()
        print('Time for {} elements: {}s'.format(each_arr_len, stop - start))
        # print('Same: {}'.format(arr_copy == sorted(arr)))
        times.append(stop - start)
    plt.scatter(times, lens)
    plt.show()
