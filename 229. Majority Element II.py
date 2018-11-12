# coding=utf-8
"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mode1 = None
        count1 = 0
        mode2 = None
        count2 = 0
        for number in nums:
            if number == mode1:
                count1 += 1
            elif number == mode2:
                count2 += 1
            elif count1 == 0:
                mode1 = number
                count1 += 1
            elif count2 == 0:
                mode2 = number
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        result = list()
        count1 = 0
        count2 = 0
        for number in nums:
            if number == mode1:
                count1 += 1
            elif number == mode2:
                count2 += 1
        if count1 > len(nums) / 3:
            result.append(mode1)
        if count2 > len(nums) / 3:
            result.append(mode2)
        return result
