# coding=utf-8
"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution(object):
    def threeSum1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def twoSum(nums, target):
            """
            hashmap
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
            """
            nums_map = {}
            for num in nums:
                if target - num in nums_map:
                    if (-target, target - num, num) not in result:
                        result.append((-target, target - num, num))
                nums_map[num] = target - num

        n = len(nums)
        nums.sort()
        result = []
        for i in range(n):
            twoSum(nums[i + 1:], 0 - nums[i])
        return [list(i) for i in result]

    def threeSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        result = list()
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                sum = nums[left] + nums[right] + nums[i]
                if sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif sum > 0:
                    right -= 1
                else:
                    left += 1
        return result


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for index, number in enumerate(nums):
            if index > 0 and number == nums[index - 1]:
                continue
            target = 0 - number

            left = index + 1
            right = len(nums) - 1
            while left < right:
                two_sum = nums[left] + nums[right]
                if two_sum == target:
                    result.append([number, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while 0 < left < len(nums) and nums[left] == nums[left - 1]:
                        left += 1
                    while len(nums) - 1 > right >= 0 and nums[right] == nums[right + 1]:
                        right -= 1
                elif two_sum > target:
                    right -= 1
                    while len(nums) - 1 > right >= 0 and nums[right] == nums[right + 1]:
                        right -= 1
                elif two_sum < target:
                    left += 1
                    while 0 < left < len(nums) and nums[left] == nums[left - 1]:
                        left += 1
        return result


print Solution().threeSum2([-1, 0, 1, 2, -1, -4])
