"""
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24
Note:
The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
"""

import sys


class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min1, min2 = sys.maxint, sys.maxint
        max1, max2, max3 = -sys.maxint, -sys.maxint, -sys.maxint
        for number in nums:
            if number <= min1:
                min2 = min1
                min1 = number
            elif min1 < number <= min2:
                min2 = number
            if number >= max1:
                max3 = max2
                max2 = max1
                max1 = number
            elif max1 > number >= max2:
                max3 = max2
                max2 = number
            elif max2 > number >= max3:
                max3 = number
        return max(min1 * min2 * max1, max1 * max2 * max3)
