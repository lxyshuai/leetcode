# coding=utf-8
"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        """
        两个节点相加并加上进位
        遇到一个list是空，则对未空list进行继续处理
        处理到最后要看下要不要加一个节点
        """
        if l1 is None or l2 is None:
            return l1 or l2

        l1_current_node = l1
        l1_pre_node = None
        l2_current_node = l2
        l2_pre_node = None
        carry = 0
        while l1_current_node and l2_current_node:
            total = l1_current_node.val + l2_current_node.val + carry
            carry = total / 10
            l1_current_node.val = total % 10
            l1_pre_node = l1_current_node
            l2_pre_node = l2_current_node
            l1_current_node = l1_current_node.next
            l2_current_node = l2_current_node.next
        if l1_current_node is None and l2_current_node is None:
            pass
        else:
            if l1_current_node is None:
                l1_pre_node.next = l2_current_node
                l1_current_node = l1_pre_node.next
            while l1_current_node:
                total = l1_current_node.val + carry
                carry = total / 10
                l1_current_node.val = total % 10
                l1_pre_node = l1_current_node
                l1_current_node = l1_current_node.next
        if carry > 0:
            l1_pre_node.next = ListNode(1)
        return l1


class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        carry = 0
        root = current = ListNode(-1)
        while l1 or l2 or carry:
            l1_value = 0
            l2_value = 0
            if l1:
                l1_value = l1.val
                l1 = l1.next
            if l2:
                l2_value = l2.val
                l2 = l2.next
            carry, value = divmod(l1_value + l2_value + carry, 10)
            current.next = ListNode(value)
            current = current.next
        return root.next
