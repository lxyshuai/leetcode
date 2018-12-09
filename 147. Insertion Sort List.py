"""
Sort a linked list using insertion sort.


A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list


Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        第一步：为了避免超时，要判断新结点是否有插入左边的必要，通过新结点与左边的邻结点比较，只有在值小于左边的邻结点才插入 
        第二步：从头结点开始，依次判断新结点插入位置，若新结点值比左边结点大，则p1指针右移。由于第一步比较，所以左边一定能找到比新结点大的结点。 
        第三步：找到新结点插入的位置，将新结点插入 
        注意：新结点插入时，需要将新结点赋予给临时结点，然后立即把新结点后面的结点拼接到新结点前一结点后，再将临时结点插入新位置，否则操作顺序一反会导致临时结点操作改变新结点后的结点！！！ 
        before_compare_node指向左边插入的位置的前一个位置，
        compare_node指向向左边插入的位置的后一个位置
        before_insert_node指向要插入节点的前一个节点
        insert_node指向要要插入的结点
        """
        if head is None or head.next is None:
            return head

        start_node = ListNode(0)
        start_node.next = head

        before_insert_node = head
        insert_node = head.next
        while insert_node:
            if before_insert_node.val <= insert_node.val:
                before_insert_node = insert_node
                insert_node = insert_node.next
                continue
            before_compare_node = start_node
            compare_node = before_compare_node.next
            while compare_node:
                if compare_node.val <= insert_node.val:
                    before_compare_node = compare_node
                    compare_node = compare_node.next
                else:
                    break
            before_insert_node.next = insert_node.next
            insert_node.next = compare_node
            before_compare_node.next = insert_node
            insert_node = before_insert_node.next
        return start_node.next
