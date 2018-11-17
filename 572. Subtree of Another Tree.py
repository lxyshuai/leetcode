"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        def does_tree1_have_tree2(tree1, tree2):
            if tree1 is None and tree2 is None:
                return True
            if tree1 is None or tree2 is None:
                return False
            if tree1.val == tree2.val:
                return does_tree1_have_tree2(tree1.left, tree2.left) and does_tree1_have_tree2(tree1.right, tree2.right)

        result = False
        if s and t:
            # 根节点相同才能开始比较
            if s.val == t.val:
                result = does_tree1_have_tree2(s, t)
            # 此处包含两种情况，第一种是根节点不同的情况，第二种是根节点相同接下来的does_tree1_have_tree2比较不同的情况。
            # 在下面的左子树还存在相同的可能，所以要继续遍历
            if not result:
                result = self.isSubtree(s.left, t)
            # 此处包含两种情况，第一种是根节点不同的情况，第二种是根节点相同接下来的does_tree1_have_tree2比较不同的情况。
            # 在下面的右子树还存在相同的可能，所以要继续遍历
            if not result:
                result = self.isSubtree(s.right, t)
        return result
