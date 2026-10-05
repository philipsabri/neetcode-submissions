class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_buy = float("inf")
        highest_profit = 0
        for price in prices:
            lowest_buy = min(lowest_buy, price)
            highest_profit = max(highest_profit, price - lowest_buy)
        return highest_profit