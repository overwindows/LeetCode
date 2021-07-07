class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        if seq == "":
            return 0
        res = []
        stack = []
        for x in seq:
            if not stack:
                assert x == '('
                stack.append(['(',0])
                res.append(0)
            else:
                if x == '(':
                    if stack[-1][1] == 0:
                        stack.append(['(',1])
                        res.append(1)
                    else:
                        stack.append(['(',0])
                        res.append(0)
                else:
                    assert x == ')'
                    if stack[-1][1] == 0:
                        res.append(0)
                        stack.pop()
                    else:
                        res.append(1)
                        stack.pop()
        return res


"""
(((((())))))()((()()))
"""