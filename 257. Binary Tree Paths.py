"""
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
Accepted
192,825
Submissions
440,682
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        def process(root, result_string):
            if root.left is None and root.right is None:
                result_string += str(root.val)
                result.append(result_string)
            else:
                if root.left:
                    process(root.left, result_string + str(root.val) + "->")
                if root.right:
                    process(root.right, result_string + str(root.val) + "->")

        if root is None:
            return []
        result = []
        process(root, "")
        return result


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        def process(root, path_list):
            if not any((root.left, root.right)):
                path_list.append(str(root.val))
                self.result.append('->'.join(path_list))
                path_list.pop(-1)
            else:
                path_list.append(str(root.val))
                if root.left:
                    process(root.left, path_list)
                if root.right:
                    process(root.right, path_list)
                path_list.pop(-1)

        if root is None:
            return []
        self.result = []
        process(root, [])
        return self.result


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        # 记录当前节点在层数
        stack = [(root, 0)]
        result = []
        path = []
        while stack:
            current_node, level = stack.pop()
            path.append(str(current_node.val))
            if current_node.right:
                stack.append((current_node.right, level + 1))
            if current_node.left:
                stack.append((current_node.left, level + 1))
                continue
            if current_node.left is None and current_node.right is None:
                result.append('->'.join(path))
                if stack:
                    _, next_node_level = stack[-1]
                    while len(path) > next_node_level:
                        path.pop()
        return result
