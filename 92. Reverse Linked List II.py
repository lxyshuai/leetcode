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
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head

        dummy = ListNode(0)
        dummy.next = head

        cur = head
        pre = dummy
        for _ in range(m - 1):
            pre = cur
            cur = cur.next
        before_node = pre
        after_node = cur

        pre = None
        for _ in range(n - m + 1):
            temp_next = cur.next
            cur.next = pre
            pre = cur
            cur = temp_next

        after_node.next = cur
        before_node.next = pre

        return dummy.next


if __name__ == '__main__':
    node1 = ListNode(3)
    node1.next = ListNode(5)
    # node1.next.next = ListNode(3)
    # node1.next.next.next = ListNode(4)
    # node1.next.next.next.next = ListNode(5)
    # node1.next.next.next.next.next = ListNode(2)
    print Solution().reverseBetween(node1, 1, 2)
