class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        
        end = 0
        maxSatisfied = 0

        N = len(customers)
        if X >= N:
            return sum(customers)
        
        for i in range(N):
            if grumpy[i] == 0:
                maxSatisfied += customers[i]
        curStaified = maxSatisfied
        # print(curStaified)
        
        while end < X:
            if grumpy[end] == 1:
                curStaified += customers[end]
            end += 1
        maxSatisfied = max(maxSatisfied, curStaified)
        # print(maxSatisfied)
        start = 1
        assert end - start +1 == X
        
        while end < N:
            # if grumpy[start] == 1:
            #     curStaified += customers[start]
            if start > 0 and grumpy[start-1] == 1:
                curStaified -= customers[start-1]
            
            if grumpy[end] == 1:
                curStaified += customers[end]
            
            maxSatisfied = max(maxSatisfied, curStaified)

            start += 1
            end += 1
        
        return maxSatisfied

            
            
