"""
Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example, given a 3-ary tree:







We should return its level order traversal:

[
     [1],
     [3,2,4],
     [5,6]
]
"""


# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = [root]
        this_level_count = 1
        next_level_count = 0
        result = []
        level_list = []
        while queue:
            current_node = queue.pop(0)
            level_list.append(current_node.val)
            this_level_count -= 1
            for children in current_node.children:
                queue.append(children)
                next_level_count += 1
            if this_level_count == 0:
                result.append(level_list)
                level_list = []
                this_level_count = next_level_count
                next_level_count = 0
        return result


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = [root]
        temp_queue = []
        result = []
        while queue:
            result.append([node.val for node in queue])
            while queue:
                current_node = queue.pop(0)
                for child in current_node.children:
                    temp_queue.append(child)
            queue, temp_queue = temp_queue, queue
        return result
