class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        sum_A = sum(A)
        if sum_A % 3:
            return False

        div = sum_A // 3
        subSum = 0
        cnt = 0
        for n in A:
            subSum += n
            if subSum == div:
                subSum = 0
                cnt+=1

        return subSum == 0 and cnt>=3
'''
[0,2,1,-6,6,-7,9,1,2,0,1]
[0,2,1,-6,6,7,9,-1,2,0,1]
[3,3,6,5,-2,2,5,1,-9,4]
[]
[1]
[3]
[3,3]
[3,3,3]
'''