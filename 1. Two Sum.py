# coding=utf-8
"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
 
"""


class Solution(object):
    def twoSum1(self, nums, target):
        """
        双指针
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 排序
        new_nums = sorted(nums)
        first = 0
        last = len(new_nums) - 1
        # 求和
        sum = new_nums[first] + new_nums[last]
        while sum != target:
            # 如果和过大,last减1
            if sum > target:
                last -= 1
            # 如果和过小,first加1
            elif sum < target:
                first += 1
            sum = new_nums[first] + new_nums[last]
        result = []
        # 防止存在重复时候,指向相同坐标
        flag = True
        for index, value in enumerate(nums):
            if value == new_nums[first] and flag == True:
                result.append(index)
                flag = not flag
            elif value == new_nums[last]:
                result.append(index)
            if len(result) == 2:
                # 排序后返回,符合输出要求
                result.sort()
                return result

    def twoSum2(self, nums, target):
        """
        hashmap
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_map = {}
        for index,num1 in enumerate(nums):
            num2 = target - num1
            if num2 in nums_map:
                result =[index, nums_map[num2]]
                result.sort()
                return result
            else:
                nums_map[num1] = index



print Solution().twoSum2([2,1],3)