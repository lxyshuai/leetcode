"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.result = []

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        self.result.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        return self.result


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        stack = [root]
        result = []
        while stack:
            current_node = stack.pop()
            result.append(current_node.val)
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
        return result
