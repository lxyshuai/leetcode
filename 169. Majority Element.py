# coding=utf-8
"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
https://segmentfault.com/a/1190000004905350
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mode = 0
        count = 0
        for number in nums:
            if count == 0:
                mode = number
                count += 1
            elif number != mode:
                count -= 1
            else:
                count += 1
        return mode
