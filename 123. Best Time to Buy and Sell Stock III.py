"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        T[day][transaction_count][has_stock]
        basecase:
        T[0][transaction_count][0] = 0 # 没有股市的时候利润=0
        T[0][transaction_count][1] = -inf # 强调1如果没有股市的时候，无法拥有库存
        T[day][0][0] = 0 # 没有交易次数的时候利润=0
        T[day][0][1] = -inf # 强调1如果没有交易次数，无法拥有库存
        递归：
        T[index][transaction_count][0] = max(T[index-1][transaction_count][0], T[index-1][transaction_count][1] + prices[index-1])
        T[index][transaction_count][1] = max(T[index-1][transaction_count][1], T[index-1][transaction_count-1][0] - prices[index-1])

        本题中需要统计k=1, k=2:
        basecase:

        递归：
        k=1
        T[index][1][0] = max(T[index-1][1][0], T[index-1][1][1] + prices[index-1])
        T[index][1][1] = max(T[index-1][1][1], T[index-1][1-1][0] - prices[index-1])
        k=2
        T[index][2][0] = max(T[index-1][2][0], T[index-1][2][1] + prices[index-1])
        T[index][2][1] = max(T[index-1][2][1], T[index-1][2-1][0] - prices[index-1])
        """
        day = len(prices)
        transaction_count = 2
        has_stock = 1
        T = [[[0 for _ in range(has_stock + 1)] for _ in range(transaction_count + 1)] for _ in range(day + 1)]

        # basecase
        for _transaction_count in range(transaction_count + 1):
            T[0][_transaction_count][0] = 0
            T[0][_transaction_count][1] = float('-inf')
        for _day in range(day + 1):
            T[_day][0][0] = 0
            T[_day][0][1] = float('-inf')

        for index, price in enumerate(prices):
            T[index + 1][2][0] = max(T[index][2][0], T[index][2][1] + price)
            T[index + 1][2][1] = max(T[index][2][1], T[index][1][0] - price)
            T[index + 1][1][0] = max(T[index][1][0], T[index][1][1] + price)
            T[index + 1][1][1] = max(T[index][1][1], T[index][0][0] - price)
        return T[len(prices)][2][0]
