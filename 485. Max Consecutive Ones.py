"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = 0
        first = 0
        last = 0
        count = 0
        while last != len(nums):
            if nums[last] == 1:
                count += 1
                last += 1
            else:
                first = last + 1
                last = first
                count = 0
            if count > max_count:
                max_count = count
        return max_count


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = 0
        count = 0
        index = 0
        while index < len(nums):
            if nums[index] == 1:
                count += 1
            else:
                max_count = max(count, max_count)
                count = 0
            index += 1
        return max(count, max_count)
