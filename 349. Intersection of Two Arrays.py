"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
"""


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        def binary_sort(nums, target):
            left = 0
            right = len(nums) - 1
            while left <= right:
                middle = left + (right - left) / 2
                if nums[middle] == target:
                    return True
                elif nums[middle] < target:
                    left = middle + 1
                else:
                    right = middle - 1
            return False

        nums1.sort()
        result = set()
        for number in nums2:
            if binary_sort(nums1, number):
                result.add(number)
        return list(result)
