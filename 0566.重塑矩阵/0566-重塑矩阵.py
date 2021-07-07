class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        output = [[0]*c for _ in range(r)]
        N = len(nums)
        M = len(nums[0])
        if c*r != M*N:
            return nums
        i = 0
        j = 0
        for n in range(N):
            for m in range(M):
                output[i][j] = nums[n][m]
                j += 1
                if j == c:
                    i+=1
                    j=0

        return output