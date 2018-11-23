"""
Given a binary tree

struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
Example:

Given the following perfect binary tree,

     1
   /  \
  2    3
 / \  / \
4  5  6  7
After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \  / \
4->5->6->7 -> NULL
"""


# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


import collections


import collections
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        queue = collections.deque([root])
        temp_queue = collections.deque()
        while queue:
            for index, node in enumerate(queue):
                if index + 1 <= len(queue) - 1:
                    node.next = queue[index + 1]
            queue[-1].next = None
            while queue:
                current_node = queue.popleft()
                if current_node.left:
                    temp_queue.append(current_node.left)
                if current_node.right:
                    temp_queue.append(current_node.right)
            queue, temp_queue = temp_queue, queue
        return

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        # 因为是完美二叉树,只用处理非叶节点，而且都是有两个孩子的
        if root and all((root.left, root.right)):
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            self.connect(root.right)
            self.connect(root.left)