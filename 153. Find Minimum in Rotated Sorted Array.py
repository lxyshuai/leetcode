# coding=utf-8
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2]
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        可以将数组分为两部分，左边为一个递增部分，右边为第二个递减部分。设置left指向第一个递增序列最后一个数，而right指向第二个递增序列第一个数
        利用二分查找,首先判断nums[middle] > nums[left],说明middle在第一个递增序列，left = middle.然后nums[middle] < nums[right]，说明middle在第二个递增序列，right=middle(判断顺序不能乱)
        """
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        left = 0
        right = len(nums) - 1
        while right - left != 1:
            middle = left + (right - left) / 2
            if nums[middle] > nums[left]:
                left = middle
            elif nums[middle] < nums[left]:
                right = middle
        return nums[right]
