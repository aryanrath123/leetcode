class Solution:
    def maxProfit(self, prices, fee):
        cash, hold = 0, -prices[0]
        for p in prices[1:]:
            cash, hold = max(cash, hold + p - fee), max(hold, cash - p)
        return cash