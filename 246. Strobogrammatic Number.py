"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:

Input:  "69"
Output: true
Example 2:

Input:  "88"
Output: true
Example 3:

Input:  "962"
Output: false
"""


class Solution(object):
    def isStrobogrammatic(self, number):
        relation = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        left = 0
        right = len(number) - 1
        while left <= right:
            if not relation.get(number[left]) or relation.get(number[left]) != number[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == '__main__':
    print Solution().isStrobogrammatic('69')
