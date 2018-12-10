"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""


# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        # 现在每个节点都添加一个克隆节点
        if head is None:
            return head
        current = head
        while current:
            temp_next = current.next
            new_node = RandomListNode(current.label)
            current.next = new_node
            new_node.next = temp_next
            current = temp_next

        # 修改克隆节点的random
        current = head
        while current:
            clone = current.next
            if current.random:
                clone.random = current.random.next
            current = clone.next

        # 分开两个链表
        dummy = result_current = RandomListNode(-1)
        current = head
        while current:
            clone = current.next
            next_temp = clone.next
            result_current.next = clone
            result_current = result_current.next
            current.next = next_temp
            current = current.next
        return dummy.next
