# coding=utf-8
"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for number in nums:
            nums[abs(number) - 1] = -1 * nums[abs(number) - 1] if nums[abs(
                number) - 1] > 0 else nums[abs(number) - 1]
        for index, number in enumerate(nums):
            if number > 0:
                result.append(index + 1)
        return result


if __name__ == '__main__':
    print Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
