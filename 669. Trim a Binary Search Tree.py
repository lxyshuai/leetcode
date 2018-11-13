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
        if root is None:
            return
        if L <= root.val <= R:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
            return root
        if root.val < L:
            return self.trimBST(root.right, L, R)
        if root.val > R:
            return self.trimBST(root.left, L, R)


# coding=utf-8
class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        # 首先找到正确的根节点
        if root is None:
            return
        while root.val < L or root.val > R:
            if root is None:
                return
            # 如果root节点的值小于L，正确的根节点在root的右子树上
            if root.val < L:
                root = root.right
            # 如果root节点的值大于R，正确的根节点在root的
            if root.val > R:
                root = root.left

        # 对root节点进行L<关于整枝,由于前面选出来的root已经符合要求，所有从root.left开始整枝
        parent = root
        left = root.left
        while left:
            if left.val < L:
                parent.left = left.right
                left = left.right
            elif left.val == L:
                left.left = None
                break
            elif left.val > L:
                parent = left
                left = left.left

        right = root.right
        parent = root
        # 对root节点进行>R关于整枝,由于前面选出来的root已经符合要求，所有从root.right开始整枝
        while right:
            if right.val > R:
                parent.right = right.left
                right = right.left
            elif right.val == R:
                right.right = None
                break
            elif right.val < R:
                parent = right
                right = right.right
        return root
