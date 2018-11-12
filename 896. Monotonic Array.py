"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.



Example 1:

Input: [1,2,2,3]
Output: true
Example 2:

Input: [6,5,4,4]
Output: true
Example 3:

Input: [1,3,2]
Output: false
Example 4:

Input: [1,2,4,5]
Output: true
Example 5:

Input: [1,1,1]
Output: true


Note:

1 <= A.length <= 50000
-100000 <= A[i] <= 100000
"""


class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        current = 0
        if A[current] > A[-1]:
            direction = -1
        elif A[current] == A[-1]:
            direction = 0
        else:
            direction = 1

        while current != len(A) - 1:
            if direction == -1:
                if A[current] < A[current + 1]:
                    return False
            elif direction == 1:
                if A[current] > A[current + 1]:
                    return False
            else:
                if A[current] != A[current + 1]:
                    return False
            current += 1
        return True


if __name__ == '__main__':
    print Solution().isMonotonic([1, 1, 1])
