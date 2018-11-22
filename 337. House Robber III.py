"""
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        unordered_map = {}

        def dfs(root):
            if root is None:
                return 0
            if root in unordered_map:
                return unordered_map[root]
            value = 0
            if root.left:
                value += dfs(root.left.left) + dfs(root.left.right)
            if root.right:
                value += dfs(root.right.left) + dfs(root.right.right)
            value = max(value + root.val, dfs(root.left) + dfs(root.right))
            unordered_map[root] = value
            return value

        return dfs(root)


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # 这种方法的递归函数返回一个大小为2的一维数组res，其中res[0]表示不包含当前节点值的最大值，res[1]表示包含当前值的最大值，
        # 那么我们在遍历某个节点时，首先对其左右子节点调用递归函数，分别得到包含与不包含左子节点值的最大值，和包含于不包含右子节点值的最大值，
        # 那么当前节点的res[0]就是左子节点两种情况的较大值加上右子节点两种情况的较大值，res[1]就是不包含左子节点值的最大值加上不包含右子节点值的最大值，和当前节点值之和，返回即可，
        def process(root):
            if root is None:
                return (0, 0)
            left = process(root.left)
            right = process(root.right)
            result = []
            result.append(max(left[0], left[1]) + max(right[0], right[1]))
            result.append(root.val + left[0] + right[0])
            return result

        return max(process(root))
