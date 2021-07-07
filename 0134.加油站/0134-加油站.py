class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        start_ixs = []
        buf = [0]*N
        for i in range(N):
            buf[i] = gas[i]-cost[i]
            if buf[i] >= 0:
                start_ixs.append(i)
        if len(start_ixs) == 0 or sum(buf) < 0:
            return -1

        for start_ix in start_ixs:
            buf = 0
            for i in range(start_ix,N+start_ix):
                buf += gas[i%N]-cost[i%N]
                if buf < 0:
                    break
            if buf >= 0:
                return start_ix 

        return -1
'''
[1,2,3,4,5]
[3,4,5,1,2]
[2,3,4]
[3,4,3]
[2,3,4]
[3,4,1]
[1]
[3]
[1]
[1]
[]
[]
[5,1,2,3,4]
[4,4,1,5,1]
[5,8,2,8]
[6,5,6,6]
'''