class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        _stack = []
        cpu = {}
        for i in range(n):
            cpu[i] = 0
        
        for log in logs:
            if len(_stack) == 0:
                pid, ps, tm = log.split(':')
                _stack.append([pid,ps,int(tm),0])
            else:
                # print(_stack)
                pid, ps, tm = log.split(':')
                tm = int(tm)

                if pid == _stack[-1][0] and ps == 'end' and _stack[-1][1] == 'start':
                    total = tm - _stack[-1][2]+1 - _stack[-1][3]
                    cpu[int(pid)] += total
                    occupied = (tm - _stack[-1][2]+1)
                    _stack.pop()
                    if len(_stack) > 0:
                        _stack[-1][3] += occupied
                else:
                    _stack.append([pid,ps,int(tm),0])
        
        output = []
        for i in range(n):
            output.append(cpu[i])
        
        return output
        
