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
        result = len(nums)
        # 遍历所有子数组,i是子数组的左边界,j是子数组的右边界
        for i in range(0, len(nums), 1):
            for j in range(i, len(nums), 1):
                min_value = min(nums[i:j + 1])
                max_value = max(nums[i:j + 1])
                # 左边数组应该是有序的,且最大值应该小于需排序数组的最小值
                # 右边数组应该是有序的,且最小值应该大于需排序数组的最大值
                if (i > 0 and nums[i - 1] > min_value) or (
                        j + 1 < len(nums) and nums[j + 1] < max_value):
                    continue
                k = 0
                while k < i:
                    if nums[k] > nums[k + 1]:
                        break
                    else:
                        k += 1
                if k != i:
                    continue
                k = j
                while k < len(nums) - 1:
                    if nums[k] > nums[k + 1]:
                        break
                    else:
                        k += 1
                if k == len(nums) - 1:
                    if i == j:
                        result = 0
                    else:
                        result = min(result, j - i + 1)
        return result


if __name__ == '__main__':
    print Solution().findUnsortedSubarray(range(200))
