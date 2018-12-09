"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        left_pre = None
        left = head
        right = head

        for _ in range(n - 1):
            right = right.next

        # 删除头节点的情况
        if right.next is None:
            return head.next

        while right.next:
            left_pre = left
            left = left.next
            right = right.next

        left_pre.next = left.next
        return head
