# coding=utf-8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None:
            return
        if head.next is None:
            return
        # 拆分成两个链表
        slow_pre = None
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head1 = head
        # 保证第一个链表长度大于等于第二个链表
        head2 = slow.next
        slow.next = None

        # 翻转第二个链表
        pre = None
        cur = head2
        while cur:
            next_temp = cur.next
            cur.next = pre
            pre = cur
            cur = next_temp

        # merge两个链表
        head1_cur = head1
        head2_cur = pre
        while head2_cur:
            head1_next = head1_cur.next
            head2_next = head2_cur.next
            head1_cur.next = head2_cur
            head2_cur.next = head1_next
            head1_cur = head1_next
            head2_cur = head2_next


if __name__ == '__main__':
    node1 = ListNode(1)
    node1.next = ListNode(2)
    node1.next.next = ListNode(3)
    node1.next.next.next = ListNode(4)
    node1.next.next.next.next = ListNode(5)
    print Solution().reorderList(node1)

    # node1.next.next.next.next.next = ListNode(2)
    # print Solution().partition(node1, 3)
