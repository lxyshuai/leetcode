"""
Given two integers n and k, you need to construct a list which contains n different positive integers ranging from 1 to n and obeys the following requirement:
Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.

If there are multiple answers, print any of them.

Example 1:
Input: n = 3, k = 1
Output: [1, 2, 3]
Explanation: The [1, 2, 3] has three different positive integers ranging from 1 to 3, and the [1, 1] has exactly 1 distinct integer: 1.
Example 2:
Input: n = 3, k = 2
Output: [1, 3, 2]
Explanation: The [1, 3, 2] has three different positive integers ranging from 1 to 3, and the [2, 1] has exactly 2 distinct integers: 1 and 2.
Note:
The n and k are in the range 1 <= k < n <= 104.
"""


class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """

        def nums_unique_diffs(nums):
            diff_count = 0
            seen = set()
            for index in range(1, n):
                diff = abs(nums[index] - nums[index - 1])
                if diff not in seen:
                    diff_count += 1
                    seen.add(diff)
            return diff_count

        def permutate(nums, current_index):
            if current_index == n:
                nums_list.append(nums[:])
            for index in range(current_index, n):
                nums[current_index], nums[index] = nums[index], nums[current_index]
                permutate(nums, current_index + 1)
                nums[current_index], nums[index] = nums[index], nums[current_index]

        nums = [index + 1 for index in range(n)]
        nums_list = []
        permutate(nums, 0)
        for nums in nums_list:
            if nums_unique_diffs(nums) == k:
                return nums


class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        result = list(range(1, n - k))
        for index in range(k + 1):
            if index % 2 == 0:
                result.append(n - k + index / 2)
            else:
                result.append(n - index / 2)
        return result
