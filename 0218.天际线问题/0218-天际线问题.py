class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        N = len(buildings)

        h = []
        res = []
        q = []

        for i in range(N):
            Li, Ri, Hi = buildings[i]
            if h:
                x,y,ix,_ = h[-1]
                
                if x == Li and y == Hi:
                    h.pop()
                    h.append([Ri,Hi,ix,0])
                else:
                    h.append([Li,Hi,i,1])
                    h.append([Ri,Hi,i,0])
            else:
                h.append([Li,Hi,i,1])
                h.append([Ri,Hi,i,0])    
        h.sort()
        heap = []

        ix = -1
        for x,y,i,s in h:
            _x, _y = -1,-1
            if q:
                if ix == i and not s:
                    ix = -1

                    for _ix in q:
                        if not s and _ix == i:
                            continue 
                        if ix < 0:
                            ix = _ix
                        
                        assert ix > -1
                        if s and buildings[_ix][2] > buildings[ix][2]:
                            ix = _ix
                        
                        if not s and _ix != i and buildings[_ix][2] > buildings[ix][2]:
                            ix = _ix
                
                if s and ix > -1 and buildings[ix][2] < y:
                    while res:
                        _x, _y = res[-1]
                        if _y < y and _x == x:
                            res.pop()
                        else:
                            break
                    res.append([x,y])
                
                if s:
                    q.append(i)
                    if buildings[i][2] > buildings[ix][2]:
                        ix = i
                
                if not s and ix > -1 and buildings[ix][2] < y:
                    res.append([x,buildings[ix][2]])
                
                if not s:
                    q.remove(i)
                    if ix == i:
                        ix = -1
                    if not q:
                        res.append([x,0])
            else:
                assert s
                while res:
                    _x, _y = res[-1]
                    if _y < y and _x == x:
                        res.pop()
                    else:
                        break
                res.append([x,y])
                q.append(i)
                if ix > -1:
                    if buildings[i][2] > buildings[ix][2]:
                        ix = i
                else:
                    ix = i
        
        return res

'''
[[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
[[0,2,3],[2,5,3]]
[[0,2,3],[2,5,5]]
[[1,2,1],[1,2,2],[1,2,3]]
[[3,7,8],[3,8,7],[3,9,6],[3,10,5],[3,11,4],[3,12,3],[3,13,2],[3,14,1]]
'''