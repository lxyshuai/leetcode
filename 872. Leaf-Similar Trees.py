"""
Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.



Note:

Both of the given trees will have between 1 and 100 nodes.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        def get_leaf_value_sequence(root, sequence):
            # basecase
            if root.left is None and root.right is None:
                sequence.append(root.val)

            if root.left:
                get_leaf_value_sequence(root.left, sequence)
            if root.right:
                get_leaf_value_sequence(root.right, sequence)

        sequence1 = []
        get_leaf_value_sequence(root1, sequence1)
        sequence2 = []
        get_leaf_value_sequence(root2, sequence2)
        return sequence1 == sequence2
