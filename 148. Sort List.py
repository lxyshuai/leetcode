"""
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def merge(l1, l2):
            cur = dummy = ListNode(0)
            while l1 and l2:
                if l1.val > l2.val:
                    cur.next = l2
                    l2 = l2.next
                else:
                    cur.next = l1
                    l1 = l1.next
                cur = cur.next
            if l1:
                cur.next = l1
            if l2:
                cur.next = l2
            return dummy.next

        def merge_sort(head):
            if head is None:
                return
            if head.next is None:
                return head
            slow_pre = None
            # 不从同一个节点开始是排除只有两个节点的情况
            slow = head
            fast = head
            slow_pre = None
            while fast and fast.next:
                slow_pre = slow
                slow = slow.next
                fast = fast.next.next
            slow_pre.next = None
            head1 = merge_sort(head)
            head2 = merge_sort(slow)
            return merge(head1, head2)

        return merge_sort(head)
