from typing import Optional, Union, TypeVar

T = TypeVar("T")


class Node:
    """
    Simple node class, takes in a value in the constructor
    """

    def __init__(self, value: T):
        """
        Initializes the node, given the type T, which is an any type

        Args:
            value (T): The value to instantiate the node with
        """
        self.value: T = value
