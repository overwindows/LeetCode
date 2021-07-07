class Solution:
    def isNumber(self, s: str) -> bool:
        s=s.lower()
        s=s.strip()
        if not s:
            return False
        if s.count('e') > 0:
            if s.count('e') > 1:
                return False
            
            base, index = s.split('e')
            
            if base and index:
                if base.startswith('+') or base.startswith('-'):
                    base = base[1:]
                if index.startswith('+') or index.startswith('-'):
                    index = index[1:]
                if not base or not index:
                    return False
                for c in index:
                    if c >= '0' and c <= '9':
                        continue
                    else:
                        return False
                
                if base.count('.') > 1 or base == '.':
                    return False
                
                for c in base:
                    if c >= '0' and c <= '9':
                        continue
                    else:
                        if c != '.':
                            return False

                return True
            else:
                return False
        else:
            if s.startswith('+') or s.startswith('-'):
                s = s[1:]
            if not s:
                return False
            if s.count('.') > 1 or s == '.':
                return False
                
            for c in s:
                if c >= '0' and c <= '9':
                    continue
                else:
                    if c != '.':
                        return False 
            
            return True