"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        result = []
        queue = [root]
        while queue:
            result.append(queue[-1].val)
            temp_queue = []
            while queue:
                current_node = queue.pop(0)
                if current_node.left:
                    temp_queue.append(current_node.left)
                if current_node.right:
                    temp_queue.append(current_node.right)
            temp_queue, queue = queue, temp_queue
        return result
