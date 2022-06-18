class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        cur_min = prices[0]
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - cur_min)
            cur_min = min(cur_min, prices[i])
        return max_profit
