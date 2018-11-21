"""
A preorder traversal is:

(root node) (preorder of left branch) (preorder of right branch)
While a postorder traversal is:

(postorder of left branch) (postorder of right branch) (root node)
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        # pre: root + left + right
        # post: left + right + root
        root = TreeNode(pre[0])
        L = TreeNode(pre[1])
        index = post.index(pre[1])
        pre_of_left = pre[1: index + 2]
        pre_of_right = pre[index + 2:]
        post_of_left = post[:index + 1]
        post_of_right = post[index + 1: -1]

        root.left = self.constructFromPrePost(pre_of_left, post_of_left)
        root.right = self.constructFromPrePost(pre_of_right, post_of_right)
        return root
