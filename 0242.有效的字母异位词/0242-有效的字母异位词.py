class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alpha = [0] * 26
        
        if len(s) != len(t):
            return False
        
        for c in s:
            alpha[ord(c)-ord('a')] += 1
        
        for c in t:
            alpha[ord(c)-ord('a')] -= 1

        for v in alpha:
            if v != 0:
                return False
        
        return True
