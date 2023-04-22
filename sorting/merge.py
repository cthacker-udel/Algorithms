from typing import List


def merge(array: List[int], p: int, q: int, r: int) -> List[int]:
    sorted_arr: List[int] = []
    arr_1 = array[p:q]
    arr_2 = array[q:r]
    for i in range(r):
        if len(arr_1) == 0:
            sorted_arr.append(arr_2[0])
            del arr_2[0]
        elif len(arr_2) == 0:
            sorted_arr.append(arr_1[0])
            del arr_1[0]
        else:
            sorted_arr.append(arr_1[0] if arr_1[0] < arr_2[0] else arr_2[0])
            if arr_1[0] < arr_2[0]:
                del arr_1[0]
            else:
                del arr_2[0]
    return sorted_arr


def merge_v2(array: List[int], p: int, q: int, r: int) -> List[int]:
    """
    Merges an array in O(n) time

    Args:
        array (List[int]): The array we are merging
        p (int): The leftmost index
        q (int): The middle index
        r (int): The rightmost index

    Returns:
        List[int]: The merged, sorted list
    """
    # number of elements in the left side
    n1 = q - p
    # number of elements in the right side
    n2 = r - q
    # the left side array
    l = [0] * n1
    # the right side array
    right_side = [0] * n2
    # loop from 0...n1
    for i in range(n1):
        # set l[i] to equal the array of p + the element we are adding so l[0] = array[p + 0], giving us the first element starting at p, and for 1, the next, and so on
        l[i] = array[p + i]
    # loop from 0...n2
    for j in range(n2):
        # set r[j] to equal the array of q + the element we are adding so r[0] = array[q + 0], giving us the first element at q, and 1 the next one, and 2 the second next one, and so on
        right_side[j] = array[q + j]
    # now that both arrays are instantiated properly, we add infinites at the end to avoid running into any issues
    l.append(float('inf'))
    right_side.append(float('inf'))
    # now we loop through the array
    l_index = 0
    r_index = 0
    print(l, right_side)
    for i in range(p, r):
        if l[l_index] < right_side[r_index]:
            array[i] = l[l_index]
            l_index += 1
        else:
            array[i] = right_side[r_index]
            r_index += 1
    print(array)


arr = [4, 5, 6, 7, 1, 2, 3, 8]
print(merge_v2(arr, 0, 4, 7))
