# coding=utf-8
"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def process(root):
            # basecase.如果到空节点，高度为0
            if root is None:
                return 0
            left_height = process(root.left)
            right_height = process(root.right)
            self.longest_path = max(self.longest_path, left_height + right_height)
            return max(left_height, right_height) + 1

        self.longest_path = 0
        process(root)
        return self.longest_path
