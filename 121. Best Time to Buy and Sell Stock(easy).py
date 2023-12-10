class Solution(object):
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0

        min_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            profit = prices[i] - min_price
            if profit > max_profit:
                max_profit = profit

        return max_profit