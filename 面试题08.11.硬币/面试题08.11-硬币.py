class Solution:
    def waysToChange(self, n: int) -> int:
        ways_1 = [0]*1000001
        ways_5 = [0]*1000001
        ways_10 = [0]*1000001
        ways_25 = [0]*1000001

        ways_1[1] = 1
        ways_5[5] = 1
        ways_25[25] = 1
        ways_10[10] = 1

        for i in range(2,n+1):
            ways_1[i] = ways_1[i-1]
            if i > 10:
                ways_10[i] = ways_10[i-10] + ways_5[i-10] + ways_1[i-10]
            if i > 5:
                ways_5[i] = ways_5[i-5] + ways_1[i-5]
            if i > 25:
                ways_25[i] = ways_25[i-25] + ways_10[i-25] + ways_5[i-25] + ways_1[i-25]

        return (ways_1[n]+ways_5[n]+ways_10[n]+ways_25[n])%1000000007
