"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        result = list()
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if i + 3 <= n - 1:
                if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                    break
            if i < n - 3:
                if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                    continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = n - 1
                while left < right:
                    sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif sum > target:
                        right -= 1
                    else:
                        left += 1
        return result
