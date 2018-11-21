"""
You need to find the largest value in each row of a binary tree.

Example:
Input:

          1
         / \
        3   2
       / \   \
      5   3   9

Output: [1, 3, 9]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        result = []
        queue = [root]
        while queue:
            temp_queue = []
            max_value = -float('inf')
            for node in queue:
                max_value = max(max_value, node.val)
            result.append(max_value)
            while queue:
                current_node = queue.pop(0)
                if current_node.left:
                    temp_queue.append(current_node.left)
                if current_node.right:
                    temp_queue.append(current_node.right)
            queue, temp_queue = temp_queue, queue
        return result
