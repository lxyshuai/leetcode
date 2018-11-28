"""
Alice and Bob have candy bars of different sizes: A[i] is the size of the i-th bar of candy that Alice has, and B[j] is the size of the j-th bar of candy that Bob has.

Since they are friends, they would like to exchange one candy bar each so that after the exchange, they both have the same total amount of candy.  (The total amount of candy a person has is the sum of the sizes of candy bars they have.)

Return an integer array ans where ans[0] is the size of the candy bar that Alice must exchange, and ans[1] is the size of the candy bar that Bob must exchange.

If there are multiple answers, you may return any one of them.  It is guaranteed an answer exists.



Example 1:

Input: A = [1,1], B = [2,2]
Output: [1,2]
Example 2:

Input: A = [1,2], B = [2,3]
Output: [1,2]
Example 3:

Input: A = [2], B = [1,3]
Output: [2,3]
Example 4:

Input: A = [1,2,5], B = [2,4]
Output: [5,4]


Note:

1 <= A.length <= 10000
1 <= B.length <= 10000
1 <= A[i] <= 100000
1 <= B[i] <= 100000
It is guaranteed that Alice and Bob have different total amounts of candy.
It is guaranteed there exists an answer.
"""


class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        A.sort()
        B.sort()
        sum_A = sum(A)
        sum_B = sum(B)
        diff = sum_A - sum_B
        current_A = 0
        current_B = 0
        while current_A < len(A) and current_B < len(B):
            current_diff = (A[current_A] - B[current_B]) * 2
            if current_diff == diff:
                return [A[current_A], B[current_B]]
            elif current_diff > diff:
                current_B += 1
            else:
                current_A += 1

        return []


class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        # A_sum - x + y = B_sum - y + x
        # y = x + (B_sum - A_sum) / 2
        A_sum = sum(A)
        B_sum = sum(B)
        B_set = set(B)
        for x in A:
            if x + (B_sum - A_sum) / 2 in B_set:
                return [x, x + (B_sum - A_sum) / 2]
