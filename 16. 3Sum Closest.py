"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        result = list()
        nums.sort()
        diff = float('inf')
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == target:
                    return target
                elif sum > target:
                    if abs(sum - target) < diff:
                        diff = abs(sum - target)
                        result = sum
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                else:
                    if abs(sum - target) < diff:
                        diff = abs(sum - target)
                        result = sum
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return result
