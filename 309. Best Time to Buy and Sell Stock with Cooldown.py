# coding=utf-8
"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        但是在“冷却时间”的情况下，i-th如果当天卖出股票，我们就无法在当天买入(i-1)-th。因此，在上面的第二个等式中T[i-1][k][0]，T[i-2][k][0]如果我们打算在i-th当天购买，我们应该实际使用。其他一切都保持不变
        T[i][k][0] = max(T[i-1][k][0], T[i-1][k][1] + prices[i])
        T[i][k][1] = max(T[i-1][k][1], T[i-2][k][0] - prices[i])
        """
        day = len(prices)
        transaction_count = len(prices) / 2
        has_stock = 1
        T = [[[0 for _ in range(has_stock + 1)] for _ in range(transaction_count + 1)] for _ in range(day + 1)]

        for _day in range(day + 1):
            T[_day][0][0] = 0
            T[_day][0][1] = float('-inf')
        for _transaction_count in range(transaction_count + 1):
            T[0][transaction_count][0] = 0
            T[0][transaction_count][1] = float('-inf')

        for index, price in enumerate(prices):
            T[index + 1][transaction_count][0] = max(T[index][transaction_count][0],
                                                     T[index][transaction_count][1] + price)
            T[index + 1][transaction_count][1] = max(T[index][transaction_count][1],
                                                     T[index - 1][transaction_count][0] - price)
        return T[day][transaction_count][0]


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        但是在“冷却时间”的情况下，i-th如果当天卖出股票，我们就无法在当天买入(i-1)-th。因此，在上面的第二个等式中T[i-1][k][0]，T[i-2][k][0]如果我们打算在i-th当天购买，我们应该实际使用。其他一切都保持不变
        T[i][k][0] = max(T[i-1][k][0], T[i-1][k][1] + prices[i])
        T[i][k][1] = max(T[i-1][k][1], T[i-2][k][0] - prices[i])
        """
        day = len(prices)
        transaction_count = len(prices) / 2
        has_stock = 1
        T_ik0 = 0
        T_ik1 = float('-inf')
        T_ik0_pre = 0
        for index, price in enumerate(prices):
            T_ik0_old = T_ik0
            T_ik0 = max(T_ik0, T_ik1 + price)
            T_ik1 = max(T_ik1, T_ik0_pre - price)
            T_ik0_pre = T_ik0_old
        return T_ik0
