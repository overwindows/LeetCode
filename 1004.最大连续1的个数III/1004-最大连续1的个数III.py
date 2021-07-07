class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        st = 0
        ed = 0
        longest = 0
        ones = 0
        N = len(A)

        while ed < N:
            ones += A[ed]
            distances = ed - st +1
            if distances <= ones + K:
                longest = max(longest, distances)
                ed += 1
            else:
                ones -= A[st]
                st += 1
        
        return longest
            

        

