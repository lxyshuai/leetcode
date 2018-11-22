"""
by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        level_result_list = []
        queue = [root]
        while queue:
            level_queue = []
            level_result = [node.val for node in queue]
            level_result_list.append(level_result)
            while queue:
                current_node = queue.pop(0)
                if current_node.left:
                    level_queue.append(current_node.left)
                if current_node.right:
                    level_queue.append(current_node.right)
            queue, level_queue = level_queue, queue
        return level_result_list
