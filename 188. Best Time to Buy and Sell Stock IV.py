# coding=utf-8
"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
"""


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        """
        T[day][transaction_count][has_stock]
        basecase:
        T[0][transaction_count][0] # 没有股市，利润=0
        T[0][transaction_count][1] # 没有股市，不能持有股票，利润=-inf
        T[day][0][0] # 没有交易次数，利润=0
        T[day][0][1] # 没有交易次数，不能持有股票，利润=-inf
        递归：
        T[day][transaction_count][0] = max(T[day - 1][transaction_count][0], T[day-1][transaction_count][1] + price)
        T[day][transaction_count][1] = max(T[day - 1][transaction_count][1], T[day-1][transaction_count-1][0] - price)
        """
        day = len(prices)
        transaction_count = k
        has_stock = 1
        T = [[[0 for _ in range(has_stock + 1)] for _ in range(transaction_count + 1)] for _ in range(day + 1)]
        for _k in range(k + 1):
            T[0][_k][0] = 0
            T[0][_k][1] = float('-inf')
        for index in range(len(prices) + 1):
            T[index][0][0] = 0
            T[index][0][1] = float('-inf')
        if transaction_count >= len(prices):
            for index, price in enumerate(prices):
                T[index + 1][transaction_count][0] = max(T[index][transaction_count][0],
                                                         T[index][transaction_count][1] + price)
                T[index + 1][transaction_count][1] = max(T[index][transaction_count][1],
                                                         T[index][transaction_count][0] - price)
            return T[len(prices)][k][0]

        for index, price in enumerate(prices):
            for _transaction_count in range(1, transaction_count + 1):
                T[index + 1][transaction_count][0] = max(T[index][transaction_count][0],
                                                         T[index][transaction_count][1] + price)
                T[index + 1][transaction_count][1] = max(T[index][transaction_count][1],
                                                         T[index][transaction_count - 1][0] - price)
        return T[day][transaction_count][0]


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        """
        T[day][transaction_count][has_stock]
        basecase:
        T[0][transaction_count][0] # 没有股市，利润=0
        T[0][transaction_count][1] # 没有股市，不能持有股票，利润=-inf
        T[day][0][0] # 没有交易次数，利润=0
        T[day][0][1] # 没有交易次数，不能持有股票，利润=-inf
        递归：
        T[day][transaction_count][0] = max(T[day - 1][transaction_count][0], T[day-1][transaction_count][1] + price)
        T[day][transaction_count][1] = max(T[day - 1][transaction_count][1], T[day-1][transaction_count-1][0] - price)
        """
        day = len(prices)
        transaction_count = k
        has_stock = 1
        if transaction_count >= len(prices):
            T_ik0 = 0
            T_ik1 = float('-inf')
            for index, price in enumerate(prices):
                T_ik0 = max(T_ik0, T_ik1 + price)
                T_ik1 = max(T_ik1, T_ik0 - price)
            return T_ik0

        T_ik0 = [0 for _ in range(transaction_count + 1)]
        T_ik1 = [float('-inf') for _ in range(transaction_count + 1)]

        for index, price in enumerate(prices):
            for _transaction_count in range(1, transaction_count + 1):
                old_T_ik0 = T_ik0[_transaction_count - 1]
                T_ik0[_transaction_count] = max(T_ik0[_transaction_count], T_ik1[_transaction_count] + price)
                T_ik1[_transaction_count] = max(T_ik1[_transaction_count], old_T_ik0 - price)
        return T_ik0[transaction_count]


if __name__ == '__main__':
    print Solution().maxProfit(2, [3, 2, 6, 5, 0, 3])
