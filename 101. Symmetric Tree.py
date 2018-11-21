"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def is_mirror(t1, t2):
            if t1 is None and t2 is None:
                return True
            if t1 is None or t2 is None:
                return False
            return t1.val == t2.val and is_mirror(t1.left, t2.right) and is_mirror(t1.right, t2.left)

        return is_mirror(root, root)


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        p = [root]
        q = [root]
        while p and q:
            p_current_node = p.pop()
            q_current_node = q.pop()
            if p_current_node is None and q_current_node is None:
                continue
            if p_current_node is None or q_current_node is None:
                return False
            if p_current_node.val != q_current_node.val:
                return False
            p.append(p_current_node.left)
            p.append(p_current_node.right)
            q.append(q_current_node.right)
            q.append(q_current_node.left)
        return True


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def is_mirror(root1, root2):
            if all((root1, root2)):
                if root1.val == root2.val:
                    return is_mirror(root1.left, root2.right) and is_mirror(root1.right, root2.left)
                else:
                    return False
            else:
                if not any((root1, root2)):
                    return True
                else:
                    return False

        return is_mirror(root, root)


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        p = [root]
        q = [root]
        while p and q:
            p_current_node = p.pop()
            q_current_node = q.pop()
            if all((p_current_node, q_current_node)):
                if p_current_node.val != q_current_node.val:
                    return False
            else:
                if not any((p_current_node, q_current_node)):
                    continue
                else:
                    return False
            p.append(p_current_node.left)
            p.append(p_current_node.right)
            q.append(q_current_node.right)
            q.append(q_current_node.left)
        return True
