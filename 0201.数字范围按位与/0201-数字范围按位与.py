class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if n%2:
            n = n-1 
        if m == 0:
            return 0
        if m>=n:
            return m 

        m_ub = int(math.log(m,2))+1
        n_lb = int(math.log(n,2))

        #print(m_ub,n_lb)
        if n_lb > m_ub:
            return 0        
        elif n_lb < m_ub:
            if m % 2:
                return m & (2**n_lb | self.rangeBitwiseAnd(m+1-2**n_lb, n-2**n_lb))
            else:
                return 2**n_lb | self.rangeBitwiseAnd(m-2**n_lb, n-2**n_lb)
        else:
            return 2**n_lb & m

"""
10
12
4
8
12
14
5
7
0
1
"""