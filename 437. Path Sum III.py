# coding=utf-8
"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import collections


class Solution(object):
    def __init__(self):
        self.count = 0

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        def find_sum(root, total_sum):
            if root is None:
                return
            # total_sum记录的是从root到当前节点的总和
            total_sum += root.val
            # part_sums[total_sum - sum]记录了之前有没有出现过这个部分和，如果出现过，则说明存在total_sum - sum的部分路径和
            self.count += part_sums[total_sum - sum]
            # 把到当前节点的总和当成一个部分和记录
            part_sums[total_sum] += 1
            find_sum(root.left, total_sum)
            find_sum(root.right, total_sum)
            part_sums[total_sum] -= 1

        # 用于记录从root出发到任意节点的的部分和出现的次数
        part_sums = collections.Counter([0])
        find_sum(root, 0)
        return self.count


class Solution(object):
    def __init__(self):
        self.count = 0
        self.part_sums = collections.Counter([0])
        self.total_sum = 0

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root is None:
            return 0
        self.total_sum += root.val
        self.count += self.part_sums[self.total_sum - sum]
        self.part_sums[self.total_sum] += 1
        self.pathSum(root.left, sum)
        self.pathSum(root.right, sum)
        self.part_sums[self.total_sum] -= 1
        self.total_sum -= root.val
        return self.count
