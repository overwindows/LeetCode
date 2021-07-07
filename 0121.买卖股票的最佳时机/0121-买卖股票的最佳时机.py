class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = sys.maxsize
        cur_profit = 0
        N = len(prices)
        for i in range(N):
            cur_min = min(prices[i], cur_min)
            cur_profit = max(cur_profit, prices[i]-cur_min)

        return cur_profit
