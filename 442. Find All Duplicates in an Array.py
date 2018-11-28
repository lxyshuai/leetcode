# coding=utf-8
"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for index, number in enumerate(nums):
            real_number = abs(number)
            if nums[real_number - 1] < 0:
                result.append(real_number)
            else:
                nums[real_number - 1] *= -1
        return result


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for number in nums:
            real_number = abs(number)
            if nums[real_number - 1] < 0:
                result.append(real_number)
            else:
                nums[real_number - 1] = -1 * nums[real_number - 1]
        return result

