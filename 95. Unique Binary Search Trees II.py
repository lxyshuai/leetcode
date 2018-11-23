"""
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        def generate_trees(start, end):
            # 相等的时候返回本身，超过就返回None
            if start > end:
                return [None]
            all_trees = []

            for i in range(start, end + 1):
                left_trees = generate_trees(start, i - 1)
                right_trees = generate_trees(i + 1, end)

                for left_tree in left_trees:
                    for right_tree in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = left_tree
                        current_tree.right = right_tree
                        all_trees.append(current_tree)
            return all_trees

        return generate_trees(1, n) if n else []
