# coding=utf-8
"""
Given a (singly) linked list with head node root, write a function to split the linked list into k consecutive linked list "parts".

The length of each part should be as equal as possible: no two parts should have a size differing by more than 1. This may lead to some parts being null.

The parts should be in order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal parts occurring later.

Return a List of ListNode's representing the linked list parts that are formed.

Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]
Example 1:
Input:
root = [1, 2, 3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The input and each element of the output are ListNodes, not arrays.
For example, the input root has root.val = 1, root.next.val = 2, \root.next.next.val = 3, and root.next.next.next = null.
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but it's string representation as a ListNode is [].
Example 2:
Input:
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
Note:

The length of root will be in the range [0, 1000].
Each value of a node in the input will be an integer in the range [0, 999].
k will be an integer in the range [1, 50].
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        current = root
        length = 0
        while current:
            current = current.next
            length += 1

        width, remainder = divmod(length, k)
        result = []
        for _k in range(k):
            head = current = ListNode(-1)
            for _width in range(width + (1 if remainder else 0)):
                new_node = ListNode(root.val)
                current.next = new_node
                current = new_node
                root = root.next
            remainder = remainder - 1 if remainder > 0 else 0
            result.append(head.next)
        return result


class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        current = root
        length = 0
        while current:
            current = current.next
            length += 1

        width, remainder = divmod(length, k)
        current = root
        result = []
        for _k in range(k):
            head = current
            # 由于本身已经是第一个节点需要-1
            for _width in range(width + (1 if remainder else 0) - 1):
                # 后面为cur可能为None,需要判断
                if current:
                    current = current.next
            # 后面为cur可能为None,需要判断
            if current:
                current.next, current = None, current.next
            remainder = remainder - 1 if remainder > 0 else 0
            result.append(head)
        return result
