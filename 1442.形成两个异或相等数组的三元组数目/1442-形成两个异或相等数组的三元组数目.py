class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        N = len(arr)
        xor = [0] * N
        xor[0] = arr[0]

        cnt = 0
        for i in range(1,N):
            xor[i] = xor[i-1]^arr[i]
            if xor[i] == 0:
                cnt += i
                # print(arr[:i+1],i)

        for i in range(N-1):
            for k in range(i+1,N):
                xor_i_k = xor[k]^xor[i]
                if xor_i_k == 0:
                    cnt += (k-i-1)
                    # print(arr[i+1:k+1],(k-i-1))

        return cnt

"""
[2,3,1,6,7]
[1,1,1,1,1]
[2,3]
[1,3,5,7,9]
[7,11,12,9,5,2,7,17,22]
"""
        