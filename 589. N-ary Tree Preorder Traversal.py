"""
Given an n-ary tree, return the preorder traversal of its nodes' values.

For example, given a 3-ary tree:







Return its preorder traversal as: [1,3,5,6,2,4].



Note:

Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []

        def process(root):
            if root is None:
                return
            result.append(root.val)
            for children in root.children:
                process(children)

        process(root)
        return result


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        result = []
        stack = []
        stack.append(root)
        while stack:
            current_node = stack.pop()
            result.append(current_node.val)
            for children in reversed(current_node.children):
                stack.append(children)
        return result
