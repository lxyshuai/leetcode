# coding=utf-8
"""
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Example 1:
Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

Example 2:
Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

Follow Up:
Can you do it in O(n) time?
"""


class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        index遍历nums，计算0~index的sum(用一个dict记录某个sum第一次出现的index)，如果sum - k 在字典中更新maxlen
        """
        max_length = 0
        sum_dict = {}
        before_sum = 0
        for index, number in enumerate(nums):
            current_sum = before_sum + number
            if current_sum == k:
                max_length = max(max_length, index + 1)
            else:
                if current_sum - k in sum_dict:
                    max_length = max(max_length, index - sum_dict[current_sum - k])

            if current_sum not in sum_dict:
                sum_dict[current_sum] = index
            before_sum = current_sum
        return max_length


if __name__ == '__main__':
    print Solution().maxSubArrayLen([1, -1, 5, -2, 3], 3)
    print Solution().maxSubArrayLen([-2, -1, 2, 1], 1)
