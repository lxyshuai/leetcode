"""
Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.
Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1.
Note: Length of the array will not exceed 10,000.
"""

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 1:
            return nums
        max_count = 0
        first = 0
        last = 0
        while last != len(nums):
            if last == 0:
                max_count += 1
            elif nums[last] > nums[last - 1]:
                max_count = max(max_count, last - first + 1)
            else:
                max_count = 1
                first = last
            last += 1
        return max_count