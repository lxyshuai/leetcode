"""
Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Note:

0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.
"""


class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        """
        T[i][k][0] = max(T[i-1][k][0], T[i-1][k][1] + prices[i])
        T[i][k][1] = max(T[i-1][k][1], T[i-1][k][0] - prices[i] - fee)
        """
        day = len(prices)
        transaction_count = len(prices) / 2
        has_stock = 1

        T = [[[0 for _ in range(has_stock + 1)] for _ in range(transaction_count + 1)] for _ in range(day + 1)]

        for _day in range(day + 1):
            T[_day][0][0] = 0
            T[_day][0][1] = float('-inf')
        for _transaction_count in range(transaction_count + 1):
            T[0][_transaction_count][0] = 0
            T[0][_transaction_count][1] = float('-inf')

        for index, price in enumerate(prices):
            T[index + 1][transaction_count][0] = max(T[index][transaction_count][0],
                                                     T[index][transaction_count][1] + price)
            T[index + 1][transaction_count][1] = max(T[index][transaction_count][1],
                                                     T[index][transaction_count][0] - price - fee)
        return T[day][transaction_count][0]


class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        day = len(prices)
        transaction_count = len(prices) / 2
        has_stock = 1

        T_ik0 = 0
        T_ik1 = float('-inf')

        for price in prices:
            old_T_ik0 = T_ik0
            T_ik0 = max(T_ik0, T_ik1 + price)
            T_ik1 = max(T_ik1, old_T_ik0 - price - fee)
        return T_ik0
