"""
Given a tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.

Example 1:
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \
1        7   9

Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

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
            \
             7
              \
               8
                \
                 9
Note:

The number of nodes in the given tree will be between 1 and 100.
Each node will have a unique integer value from 0 to 1000.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def process(root, last_node):
            if root is None:
                return last_node

            current_last_node = process(root.left, last_node)
            current_last_node.right = root
            root.left = None
            return process(root.right, root)

        new_node = TreeNode(0)
        process(root, new_node)
        return new_node.right


class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        head = last_node = TreeNode(0)
        if root is None:
            return
        stack = []
        current_node = root
        while stack or current_node:
            if current_node:
                stack.append(current_node)
                current_node = current_node.left
            else:
                current_node = stack.pop()
                last_node.right = current_node
                current_node.left = None
                last_node = current_node
                current_node = current_node.right
        return head.right


class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def process(root):
            if root is None:
                return
            process(root.left)
            self.parent.right = root
            root.left = None
            self.parent = root
            process(root.right)

        self.parent = TreeNode(-1)
        new_root = self.parent
        process(root)
        return new_root.right


class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def process(root):
            if root is None:
                return
            process(root.left)
            self.parent.right = root
            root.left = None
            self.parent = root
            process(root.right)

        self.parent = TreeNode(-1)
        new_root = self.parent
        process(root)
        return new_root.right


if __name__ == '__main__':
    node1 = TreeNode(5)
    node2 = TreeNode(3)
    node3 = TreeNode(6)
    node4 = TreeNode(2)
    node5 = TreeNode(4)
    node6 = TreeNode(8)
    node7 = TreeNode(1)
    node8 = TreeNode(7)
    node9 = TreeNode(9)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.right = node6
    node4.left = node7
    node6.left = node8
    node6.right = node9

    Solution().increasingBST(node1)
