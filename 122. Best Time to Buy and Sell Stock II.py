"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
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
        profit = 0
        for index in range(len(prices) - 1):
            _profit = prices[index + 1] - prices[index]
            if _profit > 0:
                profit += _profit
        return profit


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for index, price in enumerate(prices):
            if index > 0 and price > prices[index - 1]:
                profit += price - prices[index - 1]
        return profit


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        index = 0
        valley = prices[0]
        peak = prices[0]
        max_profit = 0
        while index < len(prices) - 1:
            while index < len(prices) - 1 and prices[index] >= prices[index + 1]:
                index += 1
            valley = prices[index]
            while index < len(prices) - 1 and prices[index] <= prices[index + 1]:
                index += 1
            peak = prices[index]
            max_profit += peak - valley
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

        本题不限制交易次数，我们可以认为
        k = len(prices) / 2 
        """
        k = len(prices) / 2
        T = [[[0 for _ in range(2)] for _ in range(k + 1)] for _ in range(len(prices) + 1)]
        for _k in range(k + 1):
            T[0][_k][0] = 0
            T[0][_k][1] = float('-inf')
        for index in range(len(prices) + 1):
            T[index][0][0] = 0
            T[index][0][1] = float('-inf')
        for index, price in enumerate(prices):
            T[index + 1][k][0] = max(T[index][k][0], T[index][k][1] + price)
            T[index + 1][k][1] = max(T[index][k][1], T[index][k][0] - price)
        return T[len(prices)][k][0]


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

        本题不限制交易次数，我们可以认为
        T[i-1][k-1][0] = T[i-1][k][0]
        T[i-1][k-1][1] = T[i-1][k][1]

        递归关系可以化简为
        T[i][k][0] = max(T[i-1][k][0], T[i-1][k][1] + prices[i])
        T[i][k][1] = max(T[i-1][k][1], T[i-1][k-1][0] - prices[i]) = max(T[i-1][k][1], T[i-1][k][0] - prices[i])

        O(n)时间和O(1)空间
        """
        T_ik0 = 0
        T_ik1 = float('-inf')

        for index, price in enumerate(prices):
            old_Tik0 = T_ik0
            T_ik0 = max(T_ik0, T_ik1 + price)
            T_ik1 = max(T_ik1, T_ik0 - price)
        return T_ik0
