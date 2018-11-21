"""
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

For example, given a 3-ary tree:






We should return its max depth, which is 3.



Note:

The depth of the tree is at most 1000.
The total number of nodes is at most 5000.
"""


# Definition for a Node.
class Node(object):
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children


# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        if root.children == []:
            return 1
        max_depth = -float('inf')
        for child in root.children:
            max_depth = max(max_depth, self.maxDepth(child))
        return max_depth + 1


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        stack = []
        stack.append((1, root))
        max_depth = 1
        while stack:
            depth, current_node = stack.pop()
            max_depth = max(max_depth, depth)
            for children in current_node.children:
                stack.append((depth + 1, children))
        return max_depth


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(3)
    node3 = Node(2)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    node1.children = [node2, node3, node4]
    node2.children = [node5, node6]
    print Solution().maxDepth(node1)
