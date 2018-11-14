"""
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def averageOfLevels(self, root):
        """
        DFS
        :type root: TreeNode
        :rtype: List[float]
        """
        count_list = []
        sum_list = []
        result = []

        def process(root, level, sum_list, count_list):
            if root is None:
                return
            if level < len(sum_list):
                sum_list[level] += root.val
                count_list[level] += 1
            else:
                sum_list.append(root.val * 1.0)
                count_list.append(1)
            process(root.left, level + 1, sum_list, count_list)
            process(root.right, level + 1, sum_list, count_list)

        process(root, 0, sum_list, count_list)
        for _sum, _count in zip(sum_list, count_list):
            result.append(_sum / _count)
        return result


class Solution(object):
    def averageOfLevels(self, root):
        """
        BFS
        :type root: TreeNode
        :rtype: List[float]
        """
        result = []
        queue = []
        queue.append(root)
        while queue:
            sum = 0
            count = 0
            temp_queue = []
            while (queue):
                current_node = queue.pop(0)
                sum += current_node.val
                count += 1
                if current_node.left:
                    temp_queue.append(current_node.left)
                if current_node.right:
                    temp_queue.append(current_node.right)
            queue = temp_queue
            result.append(sum * 1.0 / count)
        return result
