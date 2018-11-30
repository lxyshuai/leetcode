# coding=utf-8
"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

import sys


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = sys.maxint
        for price in prices:
            if price < min_price:
                min_price = price
            if price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = float('inf')

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        # 遍历需要记录一个到目前为止的股票最小值
        min_price = float('inf')

        for price in prices:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
        return max_profit


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        # 遍历需要记录一个到目前为止的股票最小值
        min_price = float('inf')

        for price in prices:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
        return max_profit


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        第一个变量表示股市(0代表没有股市)，第二个变量表示最大交易次数，第三个变量表示手中股票库存
        Base cases:
        T[0][k][0] = 0 # 没有股市的时候没有利润
        T[i][0][0] = 0 # 没有交易的时候没有利润
        T[0][k][1] = -Infinity # 强调1如果没有库存或不允许交易，我们无法拥有库存
        T[i][0][1] = -Infinity # 强调1如果没有库存或不允许交易，我们无法拥有库存

        Recurrence relations:
        T[i][k][0] = max(T[i-1][k][0], T[i-1][k][1] + prices[i])
        T[i][k][1] = max(T[i-1][k][1], T[i-1][k-1][0] - prices[i])
        每个交易的特点是两个动作成对出现 - 买入和卖出，并且由于“无多重交易”限制，这两者之间不能有其他行为交错。我们可以假设只有行动购买才会改变允许的最大交易数量,
        为了找到最后一天结束时的最大利润，我们可以简单地遍历prices数组T[i][k][0]并T[i][k][1]根据上面的重复关系进行更新。最终的答案是T[i][k][0]（如果最终掌握0库存，我们总会有更大的利润）。
        """
        T = [[[0 for _ in range(2)] for _ in range(2)] for _ in range(len(prices) + 1)]
        T[0][1][0] = 0
        for index in range(len(prices) + 1):
            T[index][0][0] = 0
            T[index][0][1] = float('-inf')
        T[0][1][1] = float('-inf')
        for index, price in enumerate(prices):
            T[index + 1][1][0] = max(T[index][1][0], T[index][1][1] + price)
            T[index + 1][1][1] = max(T[index][1][1], T[index][0][0] - price)
        return T[len(prices)][1][0]


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        Base cases:
        T[0][k][0] = 0 # 没有股市的时候没有利润
        T[i][0][0] = 0 # 没有交易的时候没有利润
        T[0][k][1] = -Infinity # 强调1如果没有库存或不允许交易，我们无法拥有库存
        T[i][0][1] = -Infinity # 强调1如果没有库存或不允许交易，我们无法拥有库存

        Recurrence relations:
        T[i][k][0] = max(T[i-1][k][0], T[i-1][k][1] + prices[i])
        T[i][k][1] = max(T[i-1][k][1], T[i-1][k-1][0] - prices[i])

        k = 1,可以变为：
        Base cases:
        T[0][1][0] = 0 # 没有股市的时候没有利润
        T[i][0][0] = 0 # 没有交易的时候没有利润
        T[0][1][1] = -Infinity # 强调1如果没有库存或不允许交易，我们无法拥有库存
        T[i][0][1] = -Infinity # 强调1如果没有库存或不允许交易，我们无法拥有库存

        Recurrence relations:
        T[i][1][0] = max(T[i-1][1][0], T[i-1][1][1] + prices[i])
        T[i][1][1] = max(T[i-1][1][1], T[i-1][0][0] - prices[i]) 因为T[i][0][0] = 0所以 T[i][1][1] = max(T[i-1][1][1], - prices[i])

        注意到i-th当天的最大利润实际上仅取决于当天的利润(i-1)-th，则可以减少空间O(1)
        """
        T_i10 = 0
        T_i11 = float('-inf')
        for index, price in enumerate(prices):
            T_i10 = max(T_i10, T_i11 + price)
            T_i11 = max(T_i11, -price)
        return T_i10
