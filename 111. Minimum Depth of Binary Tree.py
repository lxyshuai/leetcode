"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        children = root.left, root.right
        if not any(children):
            return 1

        min_depth = float('inf')
        for child in children:
            if child:
                min_depth = min(self.minDepth(child), min_depth)
        return min_depth + 1


class Solution(object):
    def __init__(self):
        self.min_depth = float('inf')
        self.depth = 1

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if not any((root.left, root.right)):
            self.min_depth = min(self.min_depth, self.depth)
        else:
            self.depth += 1
            self.minDepth(root.left)
            self.minDepth(root.right)
            self.depth -= 1
        return self.min_depth
