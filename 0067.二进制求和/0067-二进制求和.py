class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = [int(_a) for _a in a]
        b = [int(_b) for _b in b]

        len_a = len(a)
        len_b = len(b)

        i,j = 0,0
        flag = 0
        res = []

        while i < len_a and j < len_b:
            c = a[len_a-i-1] + b[len_b-j-1] + flag
            if c > 1:
                flag = 1
                c = c%2
            else:
                flag = 0
            res.append(c)
            i += 1
            j += 1
        
        while i < len_a:
            c = a[len_a -i -1] + flag
            if c > 1:
                flag = 1
                c = c%2
            else:
                flag = 0
            res.append(c)
            i += 1
        
        while j < len_b:
            c = b[len_b-j-1] + flag
            if c >1:
                flag = 1
                c = c%2
            else:
                flag = 0
            res.append(c)
            j+=1
        
        if flag:
            res.append(flag)
        
        res.reverse()
        if 1 in res:
            return ''.join([str(c) for c in res])
        else:
            return '0' 

