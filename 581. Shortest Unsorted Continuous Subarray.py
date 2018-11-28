# coding=utf-8
"""
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_sorted = sorted(nums)
        if nums_sorted == nums:
            return 0
        index = 0
        left = 0
        while index < len(nums):
            if nums[index] != nums_sorted[index]:
                left = index
                break
            index += 1
        index = len(nums) - 1
        right = len(nums) - 1
        while index >= 0:
            if nums[index] != nums_sorted[index]:
                right = index
                break
            index -= 1
        if right > left:
            return right - left + 1


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_sorted = sorted(nums)
        left = len(nums)
        right = 0
        for index in range(len(nums)):
            if nums[index] != nums_sorted[index]:
                left = min(left, index)
                right = max(right, index)
        return right - left + 1 if right - left >= 0 else 0


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []
        left = len(nums)
        right = 0

        for index in range(len(nums)):
            while stack and nums[stack[-1]] > nums[index]:
                left = min(left, stack.pop())
            stack.append(index)

        stack = []
        for index in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[index]:
                right = max(right, stack.pop())
            stack.append(index)
        return right - left + 1 if right - left >= 0 else 0


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_value = float('inf')
        max_value = float('-inf')
        flag = False
        for index in range(1, len(nums)):
            if nums[index] < nums[index - 1]:
                flag = True
            if flag:
                min_value = min(min_value, nums[index])
        flag = False
        for index in range(len(nums) - 2, -1, -1):
            if nums[index] > nums[index + 1]:
                flag = True
            if flag:
                max_value = max(max_value, nums[index])

        left = 0
        right = len(nums) - 1
        while left < len(nums):
            if min_value < nums[left]:
                break
            left += 1
        while right >= 0:
            if max_value > nums[right]:
                break
            right -= 1
        return right - left + 1 if right - left >= 0 else 0


if __name__ == '__main__':
    print Solution().findUnsortedSubarray(range(200))
