"""
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
Example 2:
Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """

        def find(root, target, number_set):
            if root is None:
                return False
            if target - root.val in number_set:
                return True
            else:
                number_set.add(root.val)
            return find(root.left, target, number_set) or find(root.right, target, number_set)

        number_set = set()
        return find(root, k, number_set)


class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if root is None:
            return False
        queue = [root]
        number_set = set()
        while queue:
            current_node = queue.pop(0)
            if k - current_node.val in number_set:
                return True
            number_set.add(current_node.val)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return False


class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """

        def inorder(root, inorder_list):
            if root is None:
                return
            inorder(root.left, inorder_list)
            inorder_list.append(root.val)
            inorder(root.right, inorder_list)

        inorder_list = []
        inorder(root, inorder_list)
        left = 0
        right = len(inorder_list) - 1
        while left < right:
            sum = inorder_list[left] + inorder_list[right]
            if sum == k:
                return True
            elif sum < k:
                left += 1
            else:
                right -= 1
        return False
