# coding=utf-8
"""
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:

2
Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output:

2
Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def process(node):
            # 可以把这道题分为两个题，一是就边长，而是求路径长
            if node is None:
                return 0
            left_length = process(node.left)
            right_length = process(node.right)
            left_arrow = right_arrow = 0
            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1
            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1
            self.ans = max(self.ans, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)

        self.ans = 0
        process(root)
        return self.ans


class Solution(object):
    def __init__(self):
        self.longest_path = 0

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def process(node):
            if node is None:
                return 0
            left_path = process(node.left)
            right_path = process(node.right)

            if node.left and node.val == node.left.val:
                left_path += 1
            else:
                left_path = 0
            if node.right and node.val == node.right.val:
                right_path += 1
            else:
                right_path = 0

            if all((node.left, node.right)) and node.val == node.left.val == node.right.val:
                self.longest_path = max(left_path + right_path, self.longest_path)
            elif node.left and node.val == node.left.val:
                self.longest_path = max(left_path, self.longest_path)
            elif node.right and node.val == node.right.val:
                self.longest_path = max(right_path, self.longest_path)
            return max(left_path, right_path)

        process(root)
        return self.longest_path


if __name__ == '__main__':
    node1 = TreeNode(5)
    node2 = TreeNode(4)
    node3 = TreeNode(5)
    node4 = TreeNode(1)
    node5 = TreeNode(1)
    node6 = TreeNode(5)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    print Solution().longestUnivaluePath(node1)
