# coding=utf-8
"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for number in nums:
            xor ^= number
        mask = 1
        # 找到第一个异或为1的位数
        while xor & mask == 0:
            mask = mask << 1

        result1 = 0
        result2 = 0
        for number in nums:
            if number & mask:
                result1 ^= number
            else:
                result2 ^= number
        return [result1, result2]
