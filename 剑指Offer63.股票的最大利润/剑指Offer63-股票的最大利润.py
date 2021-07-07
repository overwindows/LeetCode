class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        max_profit = 0 
        init = prices.pop(0)        
        
        for price in prices:
            if price > init:
                max_profit = max(max_profit, price-init)
            elif price < init:
                init = price
            else:
                continue
        
        return max_profit
