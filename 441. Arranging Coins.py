# coding=utf-8
"""
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
"""


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """

        def coin_count_of_n_row(n):
            return n * (1 + n) / 2

        if n <= 1:
            return n

        left = 1
        right = n
        while left <= right:
            middle = left + (right - left) / 2
            count = coin_count_of_n_row(middle)
            if count > n:
                right = middle - 1
            elif count < n:
                left = middle + 1
            else:
                return middle
        return right
