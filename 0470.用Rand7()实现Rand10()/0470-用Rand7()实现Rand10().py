# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        candits = []
        for i in range(1,8):
            for j in range(1, 8):
                candits.append(i*10+j) 
        candits.sort()
        #print(candits)
        ix = {}
        n = 1
        for x in candits:
            ix[x] = n
            n += 1
        #print(ix)
        A = rand7()
        B = rand7()
        
        rnd = A*10+B

        while ix[rnd] > 40:
            A = rand7()
            B = rand7()
            rnd = A*10+B
        
        return (ix[rnd]-1) // 4 +1
            



