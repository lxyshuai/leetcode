"""
Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1:

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
The following are two duplicate subtrees:

      2
     /
    4
and

    4
Therefore, you need to return above trees' root in the form of a list.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import collections


class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        counter = collections.Counter()
        result = []

        def serial(node):
            if node is None:
                return '#'
            left_serial_string = serial(node.left)
            right_serial_string = serial(node.right)
            total_serial_string = str(node.val) + left_serial_string + right_serial_string
            counter[total_serial_string] += 1
            if counter[total_serial_string] == 2:
                result.append(node)
            return total_serial_string

        serial(root)
        return result
