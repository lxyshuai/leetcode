# coding=utf-8
"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # 如果p节点和q节点都为空，返回True
        if p is None and q is None:
            return True
        # 如果p节点为空， q不为空，返回False
        elif p is None and q is not None:
            return False
        # 如果q节点为空， p不为空，返回False
        elif p is not None and q is None:
            return False
        # 如果p和q都不为空，进一步判断
        elif p and q:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        elif p and q:
            p_stack = [p]
            q_stack = [q]
            while p_stack and q_stack:
                p_current_node = p_stack.pop()
                q_current_node = q_stack.pop()
                if p_current_node.val != q_current_node.val:
                    return False
                else:
                    if p_current_node.left and q_current_node.left:
                        p_stack.append(p_current_node.left)
                        q_stack.append(q_current_node.left)
                    elif p_current_node.left is None and q_current_node.left is None:
                        pass
                    else:
                        return False
                    if p_current_node.right and q_current_node.right:
                        p_stack.append(p_current_node.right)
                        q_stack.append(q_current_node.right)
                    elif p_current_node.right is None and q_current_node.right is None:
                        pass
                    else:
                        return False
            if not p_stack and not q_stack:
                return True
        else:
            return False
