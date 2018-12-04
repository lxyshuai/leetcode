# coding=utf-8
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 先用二分查找确定递增的部分，再在递增的部分使用二分查找才找到target
        if nums == []:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = left + (right - left) / 2
            if nums[middle] == target:
                return middle
            # 说明middle在左边的有序数组,=号只能取在这里，可以举特例[3,1]看出，等于是因为首部元素和中间元素是同一个元素
            elif nums[middle] >= nums[left]:
                if nums[middle] > target >= nums[left]:
                    right = middle - 1
                else:
                    left = middle + 1
            # 说明middle在右边的有序数组
            else:
                if nums[right] >= target > nums[middle]:
                    left = middle + 1
                else:
                    right = middle - 1
        return -1


if __name__ == '__main__':
    print Solution().search([3, 1], 1)
