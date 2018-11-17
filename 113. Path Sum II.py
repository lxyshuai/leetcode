"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        result_list = []

        def process(root, before_sum):
            if root is None:
                return
            result.append(root.val)
            if root.left is None and root.right is None:
                if before_sum + root.val == sum:
                    result_list.append(result[:])
            process(root.left, before_sum + root.val)
            process(root.right, before_sum + root.val)
            result.pop(-1)

        process(root, 0)
        return result_list
