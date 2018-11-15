"""
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.before_sum = 0

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is not None:
            self.convertBST(root.right)
            self.before_sum += root.val
            root.val = self.before_sum
            self.convertBST(root.left)
        return root


class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return

        total = 0
        stack = []
        current_node = root
        while stack or current_node:
            while current_node:
                stack.append(current_node)
                current_node = current_node.right
            current_node = stack.pop()
            total += current_node.val
            current_node.val = total
            current_node = current_node.left
        return root
