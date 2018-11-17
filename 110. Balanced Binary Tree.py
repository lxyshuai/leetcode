"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.count = 0

        def process(root):
            if root is None:
                return 0
            left_height = process(root.left)
            right_height = process(root.right)
            if abs(left_height - right_height) > 1:
                self.count += 1
            return max(left_height, right_height) + 1

        process(root)
        return self.count == 0


if __name__ == '__main__':
    # node1 = TreeNode(1)
    # node2 = TreeNode(2)
    # node3 = TreeNode(2)
    # node4 = TreeNode(3)
    # node5 = TreeNode(3)
    # node6 = TreeNode(4)
    # node7 = TreeNode(4)
    #
    # node1.left = node2
    # node1.right = node3
    # node2.left = node4
    # node2.right = node5
    # node4.left = node6
    # node4.right = node7

    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node4 = TreeNode(15)
    node5 = TreeNode(7)

    node1.left = node2
    node1.right = node3
    node3.left = node4
    node3.right = node5
    Solution().isBalanced(node1)
