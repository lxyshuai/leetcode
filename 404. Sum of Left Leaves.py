"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.left_sum = 0

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def process(root, parent):
            if root is None:
                return
            if parent.left == root and root.right is None and root.left is None:
                self.left_sum += root.val
            process(root.left, root)
            process(root.right, root)

        if root:
            process(root.left, root)
            process(root.right, root)
        return self.left_sum


class Solution(object):
    def __init__(self):
        self.left_sum = 0

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def process(root, parent):
            if root is None:
                return
            if not any((root.left, root.right)) and parent.left == root:
                self.left_sum += root.val
            else:
                process(root.left, root)
                process(root.right, root)

        if root:
            process(root.left, root)
            process(root.right, root)
        return self.left_sum
