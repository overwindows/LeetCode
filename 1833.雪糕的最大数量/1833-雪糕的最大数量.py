class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        cnt = 0
        for cost in costs:
            coins -= cost
            if coins > -1:
                cnt += 1 

        return cnt