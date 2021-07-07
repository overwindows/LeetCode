class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        cut = set()
        
        M = len(wall)
        width = sum(wall[0])
        for m in range(M):
            edge = 0
            for b in wall[m]:
                edge += b
                if edge < width:
                    cut.add(edge)

        mat = {}
        for e in cut:
            mat[e] = 0
        
        for m in range(M):
            edge = 0
            for b in wall[m]:
                edge += b 
                if edge in cut:
                    mat[edge] += 1

        _max = 0
        for _, v in mat.items():
            if v > _max:
                _max = v
        # print(_max)
        return M-_max
                
