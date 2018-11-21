# coding=utf-8
"""
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:
Input:
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
Example 2:
Input:
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = [float('inf')]

        # 根据题意可以推测出root是所有节点中的最小值，所以只需要遍历所有节点找出比root大比别的节点小的节点就可以
        def process(node):
            if node is None:
                return
            if root.val < node.val < result[0]:
                result[0] = node.val
            process(node.left)
            process(node.right)

        process(root)
        return result[0] if result[0] != float('inf') else -1


class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # 根据该二叉树的性质，可以得知二叉树的root为整个树的min
        # 所有球第二小的数，只需要找到比root大比其他节点小的节点
        def process(node):
            if node is None:
                return
            if root.val < node.val < self.second_min:
                self.second_min = node.val
            process(node.left)
            process(node.right)

        self.second_min = float('inf')
        process(root)
        return self.second_min if self.second_min != float('inf') else -1
