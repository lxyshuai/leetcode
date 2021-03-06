# coding=utf-8
"""
You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

Example 1:
Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /
  4

Output: "1(2(4))(3)"

Explanation: Originallay it needs to be "1(2(4)())(3()())",
but you need to omit all the unnecessary empty parenthesis pairs.
And it will be "1(2(4))(3)".
Example 2:
Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \
      4

Output: "1(2()(4))(3)"

Explanation: Almost the same as the first example,
except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t is None:
            return ''
        string = str(t.val)
        # 如果存在左子树及右子树
        if t.left and t.right:
            string += '(' + self.tree2str(t.left) + ')' + '(' + self.tree2str(t.right) + ')'
        # 如果左右子树都不存在
        elif t.left is None and t.right is None:
            pass
        # 左子树在，右子树不在
        elif t.left and t.right is None:
            string += '(' + self.tree2str(t.left) + ')'
        # 左子树不在，右子树在
        elif t.left is None and t.right:
            string += '(' + ')' + '(' + self.tree2str(t.right) + ')'
        return string


class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t is None:
            return ''
        result = ''
        stack = [t]
        visited_set = set()
        while stack:
            current_node = stack[-1]
            if current_node in visited_set:
                stack.pop()
                result += ')'
            else:
                visited_set.add(current_node)
                result += '(' + str(current_node.val)
                if current_node.left is None and current_node.right:
                    result += "()"
                if current_node.right:
                    stack.append(current_node.right)
                if current_node.left:
                    stack.append(current_node.left)
        return result[1:-1]
