"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        def process(nums, target, count, current_index, path):
            if target < 0:
                return
            if count == k:
                if target == 0:
                    result.append(path)
            for index in range(current_index, len(nums)):
                process(nums, target - nums[index], count + 1, index + 1, path + [nums[index]])

        result = []
        process(range(1, 10), n, 0, 0, [])
        return result
