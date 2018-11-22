"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        def process(root):
            if root is None:
                return
            left = process(root.left)
            right = process(root.right)
            if left is None:
                root.right = right
            else:
                left_end = left
                while left_end.right != None:
                    left_end = left_end.right
                left_end.right = right
                root.right = left
            root.left = None
            return root

        process(root)
