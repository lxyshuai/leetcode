"""
Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
Example 1:
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are:
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Note:
The length of the given array won't exceed 1000.
The integers in the given array are in the range of [0, 1000].
"""


class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        三条边a,b,c,构成三角形的条件: a+b>c a+c>b b+c>a
        三个数字中如果较小的两个数字之和大于第三个数字，那么任意两个数字之和都大于第三个数字，这很好证明，因为第三个数字是最大的，所以它加上任意一个数肯定大于另一个数。
        可以将问题转换为3sum变种问题
        """
        count = 0
        nums.sort()
        for first in range(0, len(nums) - 2):
            for second in range(first + 1, len(nums) - 1):
                left = second + 1
                right = len(nums) - 1
                two_sum = nums[first] + nums[second]
                while left <= right:
                    middle = left + (right - left) / 2
                    if nums[middle] >= two_sum:
                        right = middle - 1
                    elif nums[middle] < two_sum:
                        left = middle + 1
                count += right - second
        return count
