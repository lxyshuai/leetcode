"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        def get_middle_node(start_node, end_node):
            pre = None
            slow = start_node
            fast = start_node
            while True:
                pre = slow
                slow = slow.next
                fast = fast.next
                if fast is end_node:
                    break
                fast = fast.next
                if fast is end_node:
                    break
            return pre, slow, slow.next

        def process(start_node, end_node):
            if start_node is end_node:
                return TreeNode(start_node.val)
            if start_node.next is end_node:
                root = TreeNode(end_node.val)
                root.left = TreeNode(start_node.val)
                return root

            before_middle_node, middle_node, after_middle_node = get_middle_node(start_node, end_node)
            middle_tree_node = TreeNode(middle_node.val)
            middle_tree_node.left = process(start_node, before_middle_node)
            middle_tree_node.right = process(after_middle_node, end_node)
            return middle_tree_node

        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val)
        slow = head
        fast = head
        while True:
            slow = slow.next
            if fast.next:
                fast = fast.next
            else:
                break
            if fast.next:
                fast = fast.next
            else:
                break
        return process(head, fast)
