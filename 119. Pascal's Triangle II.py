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
杨辉三角主要有下列五条性质：
1.杨辉三角以正整数构成，数字左右对称，每行由1开始逐渐变大，然后变小，回到1。
2.第n行的数字个数为n个。
3.第n行的第k个数字为组合数C_{n-1}^{k-1}。
4.第n行数字和为2^{n-1}。
5.除每行最左侧与最右侧的数字以外，每个数字等于它的左上方与右上方两个数字之和（也就是说，第n行第k个数字等于第n-1行的第k-1个数字与第k个数字的和）。这是因为有组合恒等式：C_{n}^{i}=C_{n-1}^{i-1}+C_{n-1}^{i}。可用此性质写出整个杨辉三角形。

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
            for num_index in xrange(index - 1, 0, -1):
                result[num_index] = result[num_index] + result[num_index - 1]
            result.append(1)
        return result


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # 除每行最左侧与最右侧的数字以外，每个数字等于它的左上方与右上方两个数字之和（也就是说，第n行第k个数字等于第n-1行的第k-1个数字与第k个数字的和）。这是因为有组合恒等式：C_{n}^{i}=C_{n-1}^{i-1}+C_{n-1}^{i}。可用此性质写出整个杨辉三角形
        result = [0 for _ in range(rowIndex + 1)]
        result[0] = 1
        for row in range(1, rowIndex + 1):
            for index in range(row, 0, -1):
                result[index] += result[index - 1]
        return result


if __name__ == '__main__':
    print Solution().getRow(10000000)
