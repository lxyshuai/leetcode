"""
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].
"""


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        def process(cost, index):
            if index == len(cost) - 1 or index == len(cost) - 2:
                return cost[index]
            return min(cost[index] + process(cost, index + 1), cost[index] + process(cost, index + 2))
        return min(process(cost, 0), process(cost, 1))

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0 for _ in range(len(cost))]
        dp[-1] = cost[-1]
        dp[-2] = cost[-2]
        for index in range(len(cost) -3, -1, -1):
            dp[index] = cost[index] + min(dp[index + 1], dp[index + 2])
        return min(dp[0], dp[1])
