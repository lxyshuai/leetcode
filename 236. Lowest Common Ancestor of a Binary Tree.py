# coding=utf-8
"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself
             according to the LCA definition.
Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        # Variable to store LCA node.
        self.result = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def process(root):
            # 如果找到了直接直接返回False,因为第一次出现的就是LCA。
            # 除此之外后面不会后面也不会出现满足middle + left + right >= 2的情况
            if self.result is not None:
                return False

            # 遍历子树到结束，返回False:
            if root is None:
                return False
            # 递归左子树
            left = process(root.left)
            # 递归右子树
            right = process(root.right)
            # 如果该节点是p和q中间的一个
            middle = root == p or root == q

            # 如果满足middle + left + right >= 2，即左子树，右子树和本身同时包括了p和q，这意味着找到了LCA
            if middle + left + right >= 2:
                self.result = root
            # 如果该节点的左子树，右子树和本身有p,q,认为该节点包括p，q。
            return middle or left or right

        process(root)
        return self.result


class Solution(object):
    # Three static flags to keep track of post-order traversal.

    # Both left and right traversal pending for a node.
    # Indicates the nodes children are yet to be traversed.
    BOTH_PENDING = 2
    # Left traversal done.
    LEFT_DONE = 1
    # Both left and right traversal done for a node.
    # Indicates the node can be popped off the stack.
    BOTH_DONE = 0

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # Initialize the stack with the root node. The second element in the tuple
        # indicates both children of root node yet to be traversed.
        stack = [(root, Solution.BOTH_PENDING)]

        # We traverse the tree until we find both p and q.
        # This flag is set when either one of p or q is found.
        one_node_found = False

        # This is used to keep track of LCA index.
        LCA_index = -1

        # We do a post order traversal of the binary tree using stack
        while stack:

            # Peek into the top element of the stack
            parent_node, parent_state = stack[-1]

            # If the parent_state is not equal to BOTH_DONE,
            # this means the parent_node can't be popped of yet.
            # Either one or both of its children traversal is pending.
            if parent_state != Solution.BOTH_DONE:

                # If both child traversals are pending
                if parent_state == Solution.BOTH_PENDING:

                    # Check if the current parent_node is either p or q.
                    if parent_node == p or parent_node == q:

                        # If one_node_found is set already, this means we have found
                        # both the nodes. And we can return the node at LCA_index. Since,
                        # this node would be the lowest common ancestor for both p and q.
                        if one_node_found:
                            return stack[LCA_index][0]
                        else:
                            # Otherwise, set one_node_found to True,
                            # to mark one of p and q is found.
                            one_node_found = True

                            # Save the current top index of stack as the LCA_index.
                            # For the node found all the elements remaining in the
                            # stack would be its ancestors. We save the index of the lowest.
                            LCA_index = len(stack) - 1

                    # If both pending, traverse the left child first
                    child_node = parent_node.left
                else:
                    # If parent_state == Solution.LEFT_DONE
                    # traverse right child
                    child_node = parent_node.right

                # Update the node state at the top of the stack
                # Reduce it by one. Since we have visited one more child.
                stack.pop()
                stack.append((parent_node, parent_state - 1))

                # Add the child node to the stack for traversal.
                if child_node:
                    stack.append((child_node, Solution.BOTH_PENDING))
            else:

                # If the parent_state of the node is both done,
                # the top node could be popped off the stack.

                # Top node to be popped could be the ancestor node for the already found node.
                # i.e. If LCA_index is equal to length of stack. Then we decrease LCA_index by 1.
                # This helps to keep a track of the common ancestors between p and q.
                if one_node_found and LCA_index == len(stack) - 1:
                    LCA_index -= 1
                stack.pop()

        return None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        stack = [root]
        parent = {root: None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]
        return q
