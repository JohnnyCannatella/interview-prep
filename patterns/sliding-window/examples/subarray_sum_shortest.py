#!/bin/python3
import os
import unittest
from typing import List

"""
Problem: https://algo.monster/problems/subarray_sum_shortest
DATE: 10/01/25
TOPIC: sliding window, array

INPUTS:
- nums: positive integer array
- target: integer (max allowed sum)

CONSTRAINTS:
- Gli array non possono essere vuoti
- I numeri possono essere positivi

OUTPUTS:
-  intero: lunghezza del subarray più corto con somma <= target

EDGE CASES:
- Array con un solo elemento
- Target = 0
- Tutti gli elementi maggiori del target
- Somma totale dell'array minore del target

TIME: 

SPACE:

NOTES:
- La finestra è di dimensione variabile
- Dobbiamo tenere traccia della somma corrente

QUESTION: I -> INTERVIEWER - M -> Me
    M:
    I: 

"""

#nums = [1, 6, 3, 1, 2, 4, 5] and target = 10
def subarray_sum_longest(nums: List[int], target: int) -> int:
    left = 0
    window_sum = 0
    length = len(nums)
    for right in range(len(nums)):
        window_sum += nums[right]
        while window_sum >= target:
            # Aggiorna la lunghezza minima
            length = min(length, right - left + 1)
            # Riduci la finestra da sinistra
            window_sum -= nums[left]
            left+=1
    return length


class UnitTest(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(subarray_sum_longest([1,6,3,1,2,4,5], 10), 4) #normal case

if __name__ == "__main__":
    UnitTest()