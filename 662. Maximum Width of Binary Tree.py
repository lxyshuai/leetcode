"""
Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:
Input:

           1
         /   \
        3     2
       / \     \
      5   3     9

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
Example 2:
Input:

          1
         /
        3
       / \
      5   3

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
Example 3:
Input:

          1
         / \
        3   2
       /
      5

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).
Example 4:
Input:

          1
         / \
        3   2
       /     \
      5       9
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).


Note: Answer will in the range of 32-bit signed integer.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import collections


class Solution(object):
    import collections
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        max_width = 0
        queue = collections.deque([(root, 1)])
        next_level_queue = collections.deque()
        while queue:
            level_width = queue[-1][1] - queue[0][1] + 1
            max_width = max(max_width, level_width)
            while queue:
                current_node, position = queue.popleft()
                if current_node.left:
                    next_level_queue.append((current_node.left, 2 * position))
                if current_node.right:
                    next_level_queue.append((current_node.right, 2 * position + 1))
            queue, next_level_queue = next_level_queue, queue
        return max_width


class Solution(object):
    def __init__(self):
        self.result = 0

    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        level_start = []

        def dfs(node, level, index):
            if node is None:
                return
            if level == len(level_start):
                level_start.append(index)
            self.result = max(self.result, index - level_start[level] + 1)
            dfs(node.left, level + 1, 2 * index)
            dfs(node.right, level + 1, 2 * index + 1)

        dfs(root, 0, 1)
        return self.result
