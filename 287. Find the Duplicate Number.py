# coding=utf-8
"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        根据鸽笼原理，给定n + 1个范围[1, n]的整数，其中一定存在数字出现至少两次。
        利用二分查找，找出重复的数字k,取middle = left + (right - left) / 2为枚举。
        遍历数组，如果数组中小于等于middle的数量大于middle,则可以确定[1, middle]范围内一定有解,否则可以确定解落在(n / 2, n]范围内
        """
        left = 1
        right = len(nums) - 1
        while left <= right:
            middle = left + (right - left) / 2
            count = 0
            for number in nums:
                if number <= middle:
                    count += 1
            if count > middle:
                right = middle - 1
            else:
                left = middle + 1
        return left

if __name__ == '__main__':
    print Solution().findDuplicate([1,2,3,3])