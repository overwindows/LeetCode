class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        sum_len = 0
        d = {}
        for c in chars:
            if c not in d:
                d[c] = 0
            d[c]+=1
        for word in words:
            _d = d.copy()
            cover = True
            for c in word:
                if c in _d and _d[c] > 0:
                    _d[c] -= 1 
                else:
                    cover = False
                    break
            if cover:
                sum_len += len(word)
        
        return sum_len