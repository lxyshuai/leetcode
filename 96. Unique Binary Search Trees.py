"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        count_list = [0] * (n + 1)
        count_list[0], count_list[1] = 1, 1
        for index in range(2, n + 1):
            for j in range(0, index):
                count_list[index] += count_list[j] * count_list[index - j - 1]
        return count_list[n]
