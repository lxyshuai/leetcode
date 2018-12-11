class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        self.min_count = float('inf')
        def process(before_sum, index, count):
            if before_sum == amount:
                self.min_count = min(count, self.min_count)
                return
            if before_sum > amount:
                return
            if index == len(coins):
                return
            process(before_sum, index + 1, count)
            process(before_sum + coins[index], index, count + 1)
            process(before_sum + coins[index], index + 1, count + 1)
        process(0, 0, 0)
        return self.min_count if self.min_count != float('inf') else -1


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]

        for _coin in range(len(coins) + 1):
            dp[_coin][amount] = 0
        for _amount in range(amount + 1):
            dp[len(coins)][_amount] = float('inf')

        for _coin in range(len(coins) - 1, -1, -1):
            for _amount in range(amount - 1, -1, -1):
                if _amount + coins[_coin] <= amount:
                    dp[_coin][_amount] = min(dp[_coin + 1][_amount], 1 + dp[_coin][_amount + coins[_coin]],
                                             1 + dp[_coin + 1][_amount + coins[_coin]])
                else:
                    dp[_coin][_amount] = dp[_coin + 1][_amount]

        return dp[0][0] if dp[0][0] != float('inf') else - 1


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins or amount == 0:
            return 0
        dp = [float('inf') for _ in range(amount + 1)]
        dp[-1] = 0
        for _amount in range(amount - 1, -1, -1):
            for coin in coins:
                if coin + _amount <= amount:
                    dp[_amount] = min(dp[_amount], 1 + dp[coin + _amount])

        return dp[0] if dp[0] != float('inf') else -1