# coding=utf-8
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if nums == []:
            return False
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = left + (right - left) / 2
            if target == nums[middle]:
                return True
            # middle在第二个递增区间
            elif nums[right] > nums[middle]:
                if nums[right] >= target > nums[middle]:
                    left = middle + 1
                else:
                    right = middle - 1
            # middle在第一个递增区间
            elif nums[right] < nums[middle]:
                if nums[middle] > target >= nums[left]:
                    right = middle - 1
                else:
                    left = middle + 1
            elif nums[right] == nums[middle]:
                right -= 1
        return False
