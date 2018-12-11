"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def process(index):
            if index == len(nums) - 1:
                return 1
            result = 0
            for next in range(index + 1, len(nums)):
                if nums[index] < nums[next]:
                    result = max(result, process(next))
            return result + 1

        result = 0
        for index in range(len(nums)):
            result = max(result, process(index))
        return result


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1 for _ in range(len(nums))]
        for index in range(len(nums) - 2, -1, -1):
            for next_index in range(index + 1, len(nums)):
                if nums[index] < nums[next_index]:
                    dp[index] = max(dp[index], 1 + dp[next_index])
        return max(dp)


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def binary_search(nums, target):
            left = 0
            right = len(nums)
            while left <= right:
                middle = left + (right - left) / 2
                if nums[middle] >= target:
                    right = middle - 1
                else:
                    left = middle + 1
            return right + 1

        ends = []
        for number in nums:
            if not ends:
                ends.append(number)
                continue
            if number > ends[-1]:
                ends.append(number)
            elif number < ends[0]:
                ends[0] = number
            else:
                ends[binary_search(ends, number)] = number
        return len(ends)


if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print Solution().lengthOfLIS(nums)
