from __future__ import annotations

from typing import List, Optional, Union, Any

from Node import Node

from enum import Enum


class HeapConfiguration(Enum):

    MIN = 0

    MAX = 1


class HeapNode(Node):

    def __init__(self, value: Any):

        super().__init__(value)

        self.left: Optional[HeapNode] = None

        self.right: Optional[HeapNode] = None

        self.parent: Optional[HeapNode] = None


class Heap:

    def __init__(self, configuration: HeapConfiguration = HeapConfiguration.MAX, root: Optional[int] = None):
        self.elements = [root]

        self.configuration = configuration

    def insert(self, value: int) -> Heap:
        if self.elements[0] is None:
            self.elements[0] = value
        else:
            self.elements = self.elements[:] + [None]
            # check left
            self.elements[-1] = value
            currentIndex = len(self.elements) - 1
            parentInd = (len(self.elements) - 1) // 2
            while parentInd >= 0:
                if self.elements[parentInd] < value:
                    self.elements[parentInd], self.elements[currentIndex] = self.elements[currentIndex], self.elements[parentInd]
                    currentIndex = parentInd
                    parentInd = (currentIndex - 1) // 2
                else:
                    break

    def extract(self, value: int) -> Optional[int]:
        if self.elements[0] is None:
            return None
        else:
            root_element = self.elements[0]
            self.elements[0] = self.elements[-1]
            self.elements[-1] = None
            current_index = 0
            while current_index < len(self.elements):
                left_ind = (2 * current_index) + 1
                right_ind = (2 * current_index) + 2
                if self.elements[left_ind] > self.elements[current_index]:
                    self.elements[current_index], self.elements[left_ind] = self.elements[left_ind], self.elements[current_index]
                    current_index = left_ind
                elif self.elements[right_ind] > self.elements[current_index]:
                    self.elements[right_ind], self.elements[current_index] = self.elements[current_index], self.elements[right_ind]
                    current_index = right_ind
                else:
                    break

    def replace(self, value: int) -> Optional[int]:
        if self.elements[0] is None:
            return None
        else:
            self.elements[0] = value
            current_index = 0
            while current_index < len(self.elements):
                left_ind = (2 * current_index) + 1
                right_ind = (2 * current_index) + 2
                if self.elements[left_ind] > self.elements[current_index]:
                    self.elements[current_index], self.elements[left_ind] = self.elements[left_ind], self.elements[current_index]
                    current_index = left_ind
                elif self.elements[right_ind] > self.elements[current_index]:
                    self.elements[right_ind], self.elements[current_index] = self.elements[current_index], self.elements[right_ind]
                    current_index = right_ind
                else:
                    break


if __name__ == '__main__':
    heap = Heap()
    elements = [60, 47, 43, 68, 35, 99, 95]
    for each_element in elements:
        heap.insert(each_element)
    print(heap.elements)
