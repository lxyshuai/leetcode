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

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def __init__(self):
        self.length = 0

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        def reverse(head):
            if head is None:
                return head
            if head.next is None:
                self.length += 1
                return head
            return_node = reverse(head.next)
            self.length += 1
            next_temp = head.next
            next_temp.next = head
            head.next = None
            return return_node

        if head is None or k == 0:
            return head
        l1_start = cur = reverse(head)
        k = k % self.length
        if k == 0:
            l2_start = None
        else:
            for _ in range(k - 1):
                cur = cur.next
                if cur is None:
                    return l1_start
            l2_start = cur.next
            cur.next = None
        cur = l1_start = reverse(l1_start)
        l2_start = reverse(l2_start)
        while cur.next:
            cur = cur.next
        cur.next = l2_start
        return l1_start


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or k == 0:
            return head

        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1
        k = k % length

        slow = head
        fast = head
        for _ in range(k):
            fast = fast.next
        if fast is None:
            return head
        while fast.next:
            slow = slow.next
            fast = fast.next
        fast.next = head
        result = slow.next
        slow.next = None
        return result


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or k == 0:
            return head
        length = 1
        cur = head
        while cur.next:
            cur = cur.next
            length += 1
        cur.next = head

        k = k % length
        for _ in range(length - k):
            cur = cur.next
        reuslt = cur.next
        cur.next = None
        return reuslt


if __name__ == '__main__':
    node1 = ListNode(0)
    node1.next = ListNode(1)
    node1.next.next = ListNode(2)
    # node1.next.next.next = ListNode(4)
    # node1.next.next.next.next = ListNode(5)
    print Solution().rotateRight(node1, 4)
