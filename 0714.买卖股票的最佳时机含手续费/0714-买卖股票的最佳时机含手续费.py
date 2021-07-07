class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        N = len(prices)

        max_val = 0
        max_buy_val = -prices[0]-fee

        for i in range(1,N):
            max_val = max(max_val, max_buy_val + prices[i])
            max_buy_val = max(max_buy_val, max_val - prices[i] - fee)
        
        return max_val

        
        
'''
[1,3,2,8,4,9]
2
[1,3,7,5,10,3]
3
[9,8,7,1,2]
3
[4,5,2,4,3,3,1,2,5,4]
1
'''   

#