"""
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
Note:
1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].
"""


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        k_sum = sum(nums[0:k])
        max_k_sum = k_sum
        for index in range(0, len(nums) - k):
            k_sum += nums[index + k] - nums[index]
            max_k_sum = max(k_sum, max_k_sum)
        return max_k_sum * 1.0 / k
