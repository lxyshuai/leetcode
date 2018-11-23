"""
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input:
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


class Solution(object):
    def countNodes(self, root):
        def get_depth(root, is_left):
            if root is None:
                return 0
            if is_left:
                return 1 + get_depth(root.left, is_left)
            else:
                return 1 + get_depth(root.right, is_left)

        left_depth = get_depth(root, True)
        right_depth = get_depth(root, False)

        if left_depth == right_depth:
            return 2 ** left_depth - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
