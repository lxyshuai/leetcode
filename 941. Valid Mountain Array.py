"""
Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[B.length - 1]


Example 1:

Input: [2,1]
Output: false
Example 2:

Input: [3,5,5]
Output: false
Example 3:

Input: [0,3,2,1]
Output: true


Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000
"""
class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        direction = 1
        left_count = 0
        right_count = 0
        current_index = 0
        while current_index < len(A) - 1:
            if direction == 1:
                if A[current_index] < A[current_index + 1]:
                    current_index += 1
                    left_count += 1
                elif A[current_index] >= A[current_index + 1]:
                    direction = -1
            elif direction == -1:
                if A[current_index] > A[current_index + 1]:
                    right_count += 1
                    current_index += 1
                else:
                    return False
        return True if left_count > 0 and right_count > 0 else False