class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        haystack_len = len(haystack)

        if haystack_len < needle_len:
            return -1

        if needle_len == 0:
            return 0
        
        nxt = [0] * needle_len
        nxt[0] = -1
        for i in range(2, needle_len):
            if needle[i-1] == needle[nxt[i-1]]:
                nxt[i] = nxt[i-1] + 1
            else:
                ix = i-1
                nxt_ix = nxt[ix]

                while needle[i-1] != needle[nxt_ix] and nxt_ix > -1:
                    nxt_ix= nxt[nxt_ix]
                nxt[i] = nxt_ix + 1
                #print(needle[i-1], nxt[i])
        
        #print(nxt)
        k,j = 0,0
        while j < haystack_len and k < needle_len:
            if needle[k] == haystack[j]:
                k += 1
                j += 1
            else:
                if k == 0:
                    j += 1
                else:
                    k = nxt[k]

        if k == needle_len:
            return j-needle_len
        else:
            return -1