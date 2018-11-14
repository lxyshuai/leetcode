# coding=utf-8
"""
Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements lies in [L, R] (R >= L). You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.

Example 1:
Input:
    1
   / \
  0   2

  L = 1
  R = 2

Output:
    1
      \
       2
Example 2:
Input:
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

Output:
      3
     /
   2
  /
 1
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        # basecase1
        if root is None:
            return None
        # root节点符合要求
        if L <= root.val <= R:
            if root.left:
                # 对root的左子树进行剪枝
                root.left = self.trimBST(root.left, L, R)
            if root.right:
                # 对root的右子树进行剪枝
                root.right = self.trimBST(root.right, L, R)
        # root过大，不符合要求,选取左子节点为root
        if root.val > R:
            return self.trimBST(root.left, L, R)
        # root过大，不符合要求,选取右子节点为root
        if root.val < L:
            return self.trimBST(root.right, L, R)
        return root


class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if root is None:
            return root

        # 选取正确的根节点
        while root.val < L or root.val > R:
            if root is None:
                return
            elif root.val < L:
                root = root.right
            elif root.val > R:
                root = root.left

        # 对正确的根节点的左子树进行剪枝
        left = root.left
        parent = root
        while left:
            if left.val > L:
                parent = left
                left = left.left
            elif left.val == L:
                left.left = None
                break
            elif left.val < L:
                parent.left = left.right
                left = left.right

        # 对正确的根节点的右子树进行剪枝
        right = root.right
        parent = root
        while right:
            if right.val < R:
                parent = right
                right = right.right
            elif right.val == R:
                right.right = None
                break
            elif right.val > R:
                parent.right = right.left
                right = right.left
        return root
