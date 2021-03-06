# coding=utf-8
"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself
             according to the LCA definition.
Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the BST.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 因为BST的特性应该,先序遍历遇到第一个值在p~q之间的节点就是LCA
        if root is None:
            return
        # 如果遍历到p,q间其中一个，直接返回
        if root == p or root == q:
            return root
        # p和q的大小关系不确定，所以比较要有两个
        if p.val < root.val < q.val or q.val < root.val < p.val:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return left if left else right


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def process(root, p, q):
            if root is None:
                return
            # 如果遍历到p和q之间的一个，直接返回
            if root.val == p.val or root.val == q.val:
                return root
            # 根据BST的性质我们可以得知，从根节点往下找到第一个值位于p,q之间的节点就是LCA
            if p.val < root.val < q.val:
                return root
            if root.val > q.val:
                return process(root.left, p, q)
            if root.val < p.val:
                return process(root.right, p, q)

        if p.val < q.val:
            return process(root, p, q)
        else:
            return process(root, q, p)


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def process(root):
            if root is None:
                return
            if p.val <= root.val <= q.val:
                return root
            else:
                if root.val < p.val:
                    return process(root.right)
                elif root.val > q.val:
                    return process(root.left)

        if p.val < q.val:
            return process(root)
        else:
            p, q = q, p
            return process(root)
