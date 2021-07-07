class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        fib_0 = 0
        fib_1 = 1

        if n == 0:
            return fib_0
        if n == 1:
            return fib_1
        
        fib_n = -1

        for i in range(2,n+1):
            fib_n = fib_0 + fib_1
            fib_0 = fib_1
            fib_1 = fib_n
        
        return fib_n