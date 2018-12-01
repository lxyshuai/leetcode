# coding=utf-8
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

class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        思路是排序之后，从数字末尾开始往前遍历，将left指向首数字，将right之前遍历到的数字的前面一个数字，然后如果left小于right就进行循环，循环里面判断如果left指向的数加上right指向的数大于当前的数字的话，那么right到left之间的数字都可以组成三角形，这是为啥呢，相当于此时确定了i和right的位置，可以将left向右移到right的位置，中间经过的数都大于left指向的数，所以都能组成三角形，就说这思路叼不叼！加完之后，right自减一，即向左移动一位。如果left和right指向的数字之和不大于nums[i]，那么left自增1，即向右移动一位
        """
        count = 0
        nums.sort()
        for last in range(len(nums) - 1, -1, -1):
            right = last - 1
            left = 0
            while left < right:
                if nums[left] + nums[right] > nums[last]:
                    count += right - left
                    right -= 1
                else:
                    left += 1
        return count