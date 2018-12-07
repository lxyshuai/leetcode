# coding=utf-8
"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        """
        将后半部分链表翻转
        1->3->1 变成 1->3<-1
        1->2->2->1 变成 1->2->2<-1
        """
        if not head:
            return True
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        pre = None
        cur = slow
        next = cur.next
        while True:
            cur.next = pre
            pre = cur
            cur = next
            if cur is None:
                break
            next = cur.next

        while pre:
            if pre.val != head.val:
                return False
            pre = pre.next
            head = head.next
        return True

if __name__ == '__main__':
    node1 = ListNode(1)
    node1.next = ListNode(0)
    node1.next.next = ListNode(1)
    print Solution().isPalindrome(node1)