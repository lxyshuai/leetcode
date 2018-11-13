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
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def mergeTrees(self, t1, t2):
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


class Solution2(object):
    def mergeTrees(self, t1, t2):
        if not t1:
            return t2
        node_pair_stack = deque()
        node_pair_stack.append([t1, t2])
        while node_pair_stack:
            node_pair = node_pair_stack.pop()
            if node_pair[1] is None:
                continue
            node_pair[0].val += node_pair[1].val

            if node_pair[0].left is None:
                node_pair[0].left = node_pair[1].left
            else:
                node_pair_stack.append([node_pair[0].left, node_pair[1].left])

            if node_pair[0].right is None:
                node_pair[0].right = node_pair[1].right
            else:
                node_pair_stack.append([node_pair[0].right, node_pair[1].right])
        return t1
