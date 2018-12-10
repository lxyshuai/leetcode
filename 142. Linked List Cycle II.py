# coding=utf-8
"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.



Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.




Follow up:
Can you solve it without using extra space?
"""


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
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        用两个指针p1、p2指向表头，每次循环时p1指向它的后继，p2指向它后继的后继。若p2的后继为NULL，表明链表没有环；否则有环且p1==p2时循环可以终止。此时为了寻找环的入口，将p1重新指向表头且仍然每次循环都指向后继，p2每次也指向后继。当p1与p2再次相等时，相等点就是环的入口。
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                break
        else:
            return None

        index = 0
        slow = head
        while True:
            if slow is fast:
                return slow
            index += 1
            slow = slow.next
            fast = fast.next


if __name__ == '__main__':
    node1 = ListNode(3)
    node1.next = ListNode(2)
    node1.next.next = ListNode(0)
    node2 = ListNode(-1)
    node1.next.next.next = node2
    node2.next = node1.next
    print Solution().detectCycle(node1)
    # node1.next.next.next.next = ListNode(5)
    # node1.next.next.next.next.next = ListNode(2)
    # print Solution().partition(node1, 3)
