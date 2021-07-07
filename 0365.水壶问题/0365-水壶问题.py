class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:     
        # M*x - N*y = z?
        # OOM
        # state = {[[False]*(y+1) for _ in range(x+1)]} 
        state = set()
        # init state
        #state[0][0] = True
        state.add((0,0))
        if z == 0:
            return True
        #state[x][0] = True
        state.add((x,0))
        if z == x:
            return True
        #state[0][y] = True
        state.add((0,y))
        if z == y:
            return True

        #state[x][y] == True
        state.add((x,y))
        if z == x+y:
            return True

        state_queue = []

        state_queue.append((0,0))
        state_queue.append((x,y))
        state_queue.append((0,y))
        state_queue.append((x,0))

        while state_queue:
            a,b = state_queue.pop(0)
            assert a <=x and b<=y
            if a == z or b == z or a+b == z:
                return True
            # full a
            if (x,b) not in state:
                state_queue.append((x,b))
                state.add((x,b))
            # full b
            if (a,y) not in state:
                state_queue.append((a,y))
                state.add((a,y))
            # clear a
            if (0,b) not in state:
                state_queue.append((0,b))
                state.add((0,b))
            # clear b
            if (a,0) not in state:
                state_queue.append((a,0))
                state.add((a,0))

            # move a --> b
            left_b = y-b
            if a < left_b:
                _a,_b = 0,a+b
            else:
                _a,_b = a-left_b,y
            if (_a,_b) not in state:
                state_queue.append((_a,_b))
                state.add((_a,_b))
            # move b --> a
            left_a = x-a
            if b < left_a:
                _a,_b = a+b,0
            else:
                _a,_b = x, b-left_a
            if (_a,_b) not in state:
                state_queue.append((_a,_b))
                state.add((_a,_b))

        return False


'''
3
5
4
2
6
3
0
0
0
6
9
1
22003
31237
1
'''