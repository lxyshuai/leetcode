# Definition for a Node.
import collections


class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []

        def process(root):
            if root is None:
                return
            for children in root.children:
                process(children)
            result.append(root.val)

        process(root)
        return result


class Solution2(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        result = []
        stack = collections.deque()
        stack.append(root)
        while stack:
            current_node = stack.pop()
            result.append(current_node.val)
            for children in current_node.children:
                stack.append(children)
        result = result[::-1]
        return result
