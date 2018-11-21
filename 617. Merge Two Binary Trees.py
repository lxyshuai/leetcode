# coding=utf-8
"""
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7


Note: The merging process must start from the root nodes of both trees.
"""
from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    """
    :type t1: TreeNode
    :type t2: TreeNode
    :rtype: TreeNode
    """

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # 如果t1和t2都为None,则为None
        if t1 is None and t2 is None:
            return None
        # 如果t1为None，但是t2不为None，以t2为准
        elif t1 is None and t2 is not None:
            return t2
        # 如果t2为None，但是t1不为None，以t1为准
        elif t2 is None and t1 is not None:
            return t1
        # 两者都不空,t1、t2相加更新t1
        else:
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
            return t1


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        stack = deque()
        stack.append((t1, t2))
        while stack:
            t1_current_node, t2_current_node = stack.pop()
            if t1_current_node and t2_current_node:
                t1_current_node.val += t2_current_node.val

            # 如果t1_current_node和t2_current_node有左节点，将t1_current_node.left和t2_current_node.left加入等待处理
            if t1_current_node.left and t2_current_node.left:
                stack.append((t1_current_node.left, t2_current_node.left))
            # 如果t1_current_node没有左节点，t2_current_node有左节点，t1_current_node.left以t2_current_node.left为准
            elif t1_current_node.left is None and t2_current_node.left:
                t1_current_node.left = t2_current_node.left
            # 如果t1_current_node有左节点，t2_current_node没有左节点，t1_current_node.left以t1_current_node.left为准
            elif t1_current_node.left and t2_current_node.left is None:
                t1_current_node.left = t1_current_node.left
            # 如果t1_current_node和t2_current_node都没有左节点，t1_current_node.left为None
            else:
                t1_current_node.left = None

            # 如果t1_current_node和t2_current_node有右节点，将t1_current_node.right和t2_current_node.right加入等待处理
            if t1_current_node.right and t2_current_node.right:
                stack.append((t1_current_node.right, t2_current_node.right))
            # 如果t1_current_node没有右节点，t2_current_node有右节点，t1_current_node.right以t2_current_node.right为准
            elif t1_current_node.right is None and t2_current_node.right:
                t1_current_node.right = t2_current_node.right
            # 如果t1_current_node有右节点，t2_current_node没有右节点，t1_current_node.right以t1_current_node.right为准
            elif t1_current_node.right and t2_current_node.right is None:
                t1_current_node.right = t1_current_node.right
            # 如果t1_current_node和t2_current_node都没有左节点，t1_current_node.right为None
            else:
                t1_current_node.right = None
        return t1


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        stack = [(t1, t2)]
        while stack:
            t1_current_node, t2_current_node = stack.pop()
            if all([t1_current_node, t2_current_node]):
                t1_current_node.val += t2_current_node.val

            children = (t1_current_node.left, t2_current_node.left)
            if all(children):
                stack.append(children)
            else:
                for child in children:
                    if child:
                        t1_current_node.left = child

            children = (t1_current_node.right, t2_current_node.right)
            if all(children):
                stack.append(children)
            else:
                for child in children:
                    if child:
                        t1_current_node.right = child
        return t1
