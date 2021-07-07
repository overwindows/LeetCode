class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        l = list(s)
        if len(l) == 1:
            return s
        if k > 1:
            l.sort()
            return ''.join(l)
        else:
            return min(s[i:]+s[:i] for i in range(len(s)))
            
                

            