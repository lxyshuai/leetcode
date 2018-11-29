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


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for first in range(0, len(nums) - 3):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            for second in range(first + 1, len(nums) - 2):
                left = second + 1
                right = len(nums) - 1
                while left < right:
                    total_sum = nums[first] + nums[second] + nums[left] + nums[right]
                    if total_sum == target:
                        if [nums[first], nums[second], nums[left], nums[right]] not in result:
                            result.append([nums[first], nums[second], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while 0 <= right < len(nums) - 1 and nums[right] == nums[right + 1]:
                            right -= 1
                        while 0 < left <= len(nums) - 1 and nums[left] == nums[left - 1]:
                            left += 1
                    elif total_sum > target:
                        right -= 1
                        while 0 <= right < len(nums) - 1 and nums[right] == nums[right + 1]:
                            right -= 1
                    elif total_sum < target:
                        left += 1
                        while 0 < left <= len(nums) - 1 and nums[left] == nums[left - 1]:
                            left += 1
        return result


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        if len(nums) < 4:
            return []

        nums.sort()
        rst = []
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                l, r = j + 1, len(nums) - 1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s == target:
                        temp_rst = [nums[i], nums[j], nums[l], nums[r]]
                        if temp_rst not in rst:
                            rst.append(temp_rst)
                        r -= 1
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        l += 1
        return rst


if __name__ == '__main__':
    print Solution().fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0)
