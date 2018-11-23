# coding=utf-8
"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        # 如果找不到
        if root is None:
            return None
        # key > root.val,递归查找右子树
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # key > root.val,递归查找左子树
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # 找到了要被删除的节点
        elif key == root.val:
            # 如果左右节点都不存在
            if not any((root.left, root.right)):
                return None
            # 如果左节点不存在
            elif root.left is None:
                return root.right
            # 如果左节点不存在
            elif root.right is None:
                return root.left
            # 如果左右节点都存在，找到右子树的最小节点，删除
            else:
                min_node = root.right
                while min_node.left:
                    min_node = min_node.left
                min_value = min_node.val
                root.val = min_value
                root.right = self.deleteNode(root.right, min_value)
        return root
