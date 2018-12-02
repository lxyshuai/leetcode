"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
"""


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left = 0
        right = num
        while left <= right:
            middle = left + (right - left)
            temp = middle ** 2
            if temp == num:
                return True
            elif temp > num:
                right = middle - 1
            else:
                left = middle + 1
        return False


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        odd = 1
        while num > 0:
            num -= odd
            odd += 2
        return num == 0
