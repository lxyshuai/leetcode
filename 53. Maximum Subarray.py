"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

import sys


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = 0
        last = 0
        max_sum = -sys.maxint
        sum = 0
        while last != len(nums):
            sum += nums[last]
            if sum > max_sum:
                max_sum = sum
            if sum < 0:
                last += 1
                first = last
                sum = 0
            else:
                last += 1
        return max_sum


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        subarray_start_index = 0
        current_index = 0
        total_sum = 0
        max_sum = float('-inf')

        while current_index < len(nums):
            total_sum += nums[current_index]
            max_sum = max(total_sum, max_sum)
            if total_sum < 0:
                subarray_start_index = current_index + 1
                total_sum = 0
            current_index += 1
        return max_sum
