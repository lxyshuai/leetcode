# coding=utf-8
"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
"""


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dp = [0 for _ in range(len(nums))]
        if len(nums) == 0:
            pass
        else:
            self.dp[0] = nums[0]
            for index in range(1, len(nums)):
                self.dp[index] = self.dp[index - 1] + nums[index]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.dp[j]
        return self.dp[j] - self.dp[i - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
