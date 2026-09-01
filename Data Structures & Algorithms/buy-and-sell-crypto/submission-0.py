class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)
        for k in range(2, n + 1):
            for i in range(n-k + 1):
                max_profit = max(prices[i+k-1]  - prices[i], max_profit) 
        return max_profit

