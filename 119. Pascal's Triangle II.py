# coding=utf-8
"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = []
        result.append(1)
        for index in xrange(1, rowIndex + 1):
            for num_index in xrange(index-1, 0, -1):
                result[num_index] = result[num_index] + result[num_index - 1]
            result.append(1)
        return result
if __name__ == '__main__':
    print Solution().getRow(10000000)