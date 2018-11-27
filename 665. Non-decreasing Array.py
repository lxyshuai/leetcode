# coding=utf-8
"""
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
Note: The n belongs to [1, 10,000].
"""


class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 我们用count记录调整的次数
        # 调整的方法我们有两种情况：1.调整本身 2.调整前一个数
        # 原则是尽量只调整前一个数，对后面产生更小的影响
        count = 1
        index = 1
        while index <= len(nums) - 1:
            if nums[index] < nums[index - 1]:
                if count == 0:
                    return False
                # nums[index - 2]不存在或者 nums[index - 2]小于等于nums[index]
                if index - 2 == -1 or nums[index] >= nums[index - 2]:
                    nums[index - 1] = nums[index]
                else:
                    nums[index] = nums[index - 1]
                count -= 1
            index += 1
        return True
