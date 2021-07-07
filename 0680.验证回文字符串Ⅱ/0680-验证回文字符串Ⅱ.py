class Solution:
    def validPalindrome(self, s: str) -> bool:
        def _valid(s, start_ix, end_ix, flag):
            if start_ix >= end_ix:
                return True
            if s[start_ix] == s[end_ix]:
                return _valid(s, start_ix+1, end_ix-1, flag)
            else:
                if flag:
                    return _valid(s, start_ix, end_ix-1, False) or _valid(s, start_ix+1, end_ix, False)
                else:
                    return False
        
        return _valid(list(s),0,len(s)-1,True)