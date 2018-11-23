"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import collections


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = [root]
        next_level_queue = []
        this_level_direction = True
        result = []
        while queue:
            level_result = []
            if this_level_direction:
                level_result = [node.val for node in queue]
            else:
                for index in range(len(queue) - 1, -1, -1):
                    level_result.append(queue[index].val)
            result.append(level_result)
            while queue:
                current_node = queue.pop(0)
                if current_node.left:
                    next_level_queue.append(current_node.left)
                if current_node.right:
                    next_level_queue.append(current_node.right)
            this_level_direction = not this_level_direction
            queue, next_level_queue = next_level_queue, queue
        return list(result)
