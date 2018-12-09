"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
Note:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        将linked list拆分成奇偶两条链
        用两个指针交替改变执行
        """
        if head is None:
            return None
        if head.next is None:
            return head
        odd_pre = None
        odd = head
        even_start = even = head.next
        while True:
            odd.next = even.next
            odd_pre = odd
            odd = odd.next
            if not odd:
                break
            even.next = odd.next
            even = even.next
            if not even:
                break
        if even is None:
            odd.next = even_start
        elif odd is None:
            odd_pre.next = even_start
        return head
