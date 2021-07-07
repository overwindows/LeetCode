class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        def swap(L: List[int]):
            s,e = 0,len(L)-1
            while s < e:
                L[s],L[e] = L[e], L[s]
                s += 1
                e -= 1

        def flip(L: List[int]):
            for i in range(len(L)):
                L[i] = 1 - L[i]


        N = len(A)
        for i in range(N):
            swap(A[i])
            flip(A[i])

        return A


