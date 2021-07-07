class Solution:
    def compressString(self, S: str) -> str:
        ret_str = ''
        prev = None
        cnt = 0
        for c in S:
            if prev and prev == c:
                cnt += 1
            else:
                if prev:
                    ret_str += prev
                    ret_str += str(cnt)
                prev = c
                cnt = 1
        if S:
            ret_str += prev
            ret_str += str(cnt)
        if len(ret_str) < len(S):
            return ret_str
        else:
            return S
