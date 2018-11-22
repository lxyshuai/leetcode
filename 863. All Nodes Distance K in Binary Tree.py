"""
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.



Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation:
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.


Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """

        def dfs(node, parent):
            if node is None:
                return
            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)
        import collections
        queue = collections.deque([(target, 0)])
        visited = {target}
        while queue:
            # 以target为半径画圆
            if queue[0][1] == K:
                return [node.val for node, distance in queue]
            current_node, distance = queue.popleft()
            neighbour_list = [current_node.left, current_node.right, current_node.parent]
            for neighbour in neighbour_list:
                if neighbour and neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((neighbour, distance + 1))
        return []


class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        result = []

        def dfs(node):
            if node is None:
                return -1
            elif node is target:
                subtree_add(node, 0)
                return 1
            else:
                left = dfs(node.left)
                right = dfs(node.right)
                if left != -1:
                    if left == K:
                        result.append(node.val)
                    subtree_add(node.right, left + 1)
                    return left + 1
                elif right != -1:
                    if right == K:
                        result.append(node.val)
                    subtree_add(node.left, right + 1)
                    return right + 1
                else:
                    return -1

        def subtree_add(node, dist):
            if not node:
                return
            elif dist == K:
                result.append(node.val)
            else:
                subtree_add(node.left, dist + 1)
                subtree_add(node.right, dist + 1)

        dfs(root)
        return result
