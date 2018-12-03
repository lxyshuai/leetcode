# coding=utf-8
"""
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5
Explanation: Your function can return either index number 1 where the peak element is 2,
             or index number 5 where the peak element is 6.
Note:

Your solution should be in logarithmic complexity.
"""


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        二分查找，left上坡的时候变化，right下坡的时候变化
        当left==right 跳出
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = left + (right - left) / 2
            if nums[middle] < nums[middle + 1]:
                left = middle + 1
            elif nums[middle] > nums[middle + 1]:
                right = middle
        return left

# class Solution(object):
#     def findPeakElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         left = 0
#         right = len(nums) - 1
#         while left < right:
#             middle = left + (right - left) / 2
#             # 这种写法受取下中位数的影响会进入死循环
#             if nums[middle] < nums[middle - 1]:
#                 right = middle - 1
#             elif nums[middle] > nums[middle - 1]:
#                 left = middle
#         return left
