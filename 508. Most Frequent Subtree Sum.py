"""
Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Examples 1
Input:

  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in any order.
Examples 2
Input:

  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.
Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections


class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        counter = collections.Counter([])
        result = []

        def process(node):
            if node is None:
                return 0
            left_sum = process(node.left)
            right_sum = process(node.right)
            subtree_sum = left_sum + right_sum + node.val
            counter[subtree_sum] += 1
            return subtree_sum

        process(root)
        max_count = counter.most_common()[0][1]
        for value, count in counter.items():
            if count == max_count:
                result.append(value)
        return result
