"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        less_list_start_node = l_current = ListNode(0)
        equal_or_greater_list_start_node = eg_current = ListNode(0)

        while head:
            if head.val < x:
                l_current.next = head
                l_current = l_current.next
            else:
                eg_current.next = head
                eg_current = eg_current.next
            head, head.next = head.next, None
            # head.next, head = None, head.next
            # temp = head.next
            # head.next = None
            # head = temp
        l_current.next = equal_or_greater_list_start_node.next
        return less_list_start_node.next


if __name__ == '__main__':
    node1 = ListNode(1)
    node1.next = ListNode(4)
    node1.next.next = ListNode(3)
    node1.next.next.next = ListNode(2)
    node1.next.next.next.next = ListNode(5)
    node1.next.next.next.next.next = ListNode(2)
    print Solution().partition(node1, 3)
