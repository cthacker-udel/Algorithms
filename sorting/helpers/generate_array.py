from typing import List
from random import randint


def generate_array(length: int, min_value: int = 0, max_value: int = 1) -> List[int]:
    """
    Generates an array of numbers of specified length `length` with values of min <= x <= max

    Args:
        length (int): The length of the array
        min_value (int, optional): The minimum number we are placing within the array. Defaults to 0.
        max_value (int, optional): The maximum number we are placing within the array. Defaults to 1.

    Returns:
        List[int]: The generated list
    """
    return [randint(min_value, max_value + 1) for x in range(length)]
