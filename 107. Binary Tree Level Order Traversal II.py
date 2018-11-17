"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        def process(root, level):
            if root is None:
                return
            if level > len(result) - 1:
                result.append(list())

            process(root.left, level + 1)
            process(root.right, level + 1)
            result[level].append(root.val)

        result = []
        process(root, 0)
        result.reverse()
        return result


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = [root]
        this_level_count = 1
        next_level_count = 0
        result = []
        while queue:
            level_result = []
            while this_level_count != 0:
                current_node = queue.pop(0)
                this_level_count -= 1
                if current_node.left:
                    queue.append(current_node.left)
                    next_level_count += 1
                if current_node.right:
                    queue.append(current_node.right)
                    next_level_count += 1
                level_result.append(current_node.val)
            this_level_count = next_level_count
            next_level_count = 0
            result.insert(0, level_result)
        return result
