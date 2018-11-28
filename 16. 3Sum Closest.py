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


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest_diff = float('inf')
        result = float('inf')
        for index, number in enumerate(nums):
            if index > 0 and nums[index - 1] == number:
                continue

            left_index = index + 1
            right_index = len(nums) - 1

            while left_index < right_index:
                total_sum = number + nums[left_index] + nums[right_index]
                if total_sum == target:
                    return target
                elif total_sum < target:
                    left_index += 1
                    diff = abs(total_sum - target)
                    if diff < closest_diff:
                        closest_diff = diff
                        result = total_sum
                    while len(nums) > left_index > 0 and nums[left_index] == nums[left_index - 1]:
                        left_index += 1
                elif total_sum > target:
                    right_index -= 1
                    diff = abs(total_sum - target)
                    if diff < closest_diff:
                        closest_diff = diff
                        result = total_sum
                    while len(nums) - 1 > right_index >= 0 and nums[right_index] == nums[right_index + 1]:
                        right_index -= 1
        return result


if __name__ == '__main__':
    print Solution().threeSumClosest([1, 1, 1, 0], -100)
