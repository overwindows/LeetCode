class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        nopre = set(range(numCourses))
        dep = {}
        pre = {}
        for prerequisite in prerequisites:
            a, b = prerequisite

            if a in nopre:
                nopre.remove(a)

            if b in dep:
                dep[b].add(a)
            else:
                dep[b] = set([a])

            if a in pre:
                pre[a].add(b)
            else:
                pre[a] = set([b])
        # print(dep)
        # print(nopre)

        output = []
        while len(nopre) > 0:
            cand = []
            for x in nopre:
                output.append(x)

                if x in dep:
                    for xx in dep[x]:
                        pre[xx].remove(x)
                        if len(pre[xx]) == 0:
                            cand.append(xx)
                            del pre[xx]
                    
                    del dep[x]
            nopre.clear()
            for c in cand:
                nopre.add(c)

        if len(output) < numCourses:
            return []
        return output


"""
4
[[1,0],[2,0],[3,1],[3,2]]
2
[[1,0]]
1
[]
3
[[0,1],[0,2],[1,2]]
"""   
        
