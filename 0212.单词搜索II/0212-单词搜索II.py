class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Create tie tree
        tie_tree = {}
        words.sort()

        for word in words:
            node = tie_tree
            word_arr = list(word)
            word_len = len(word_arr)
            #print(word_arr, tie_tree)
            for ix in range(word_len):
                x = word_arr[ix]
                if (x not in node) and (x.upper() not in node):
                    if ix == word_len-1:
                        node[x.upper()] = {}
                    else:
                        node[x] = {}
                
                if x in node:
                    node = node[x]
                else: # x.upper() in node.
                    node = node[x.upper()]
        # Search
        M = len(board)
        N = len(board[0])
        # print(tie_tree)

        def search(mat, m, n, root, prefix):
            res = []
            # print(prefix, root, m, n)
            if not root:
                return [prefix]
            # print(mat[1][0],m,n)
            # up
            if m > 0 and mat[m-1][n] and (mat[m-1][n] in root or mat[m-1][n].upper() in root):
                v = mat[m-1][n]
                mat[m-1][n] = None

                if v in root:
                    res_up = search(mat, m-1, n, root[v], v)
                    for r in res_up:
                        res.append(prefix+r)
                else:
                    assert v.upper() in root
                    res.append(prefix+v)

                    res_up = search(mat, m-1, n, root[v.upper()], v)
                    for r in res_up:
                        res.append(prefix+r)                    
                
                mat[m-1][n] = v
            
            # down
            # print('{}-{}:{}  {}'.format(m+1,n,mat[m+1][n].upper(),root[mat[m+1][n].upper()]))
            if m+1< M and mat[m+1][n] and (mat[m+1][n] in root or mat[m+1][n].upper() in root):
                #print('Down: {}'.format(mat[m+1][n]))
                v = mat[m+1][n]
                mat[m+1][n] = None
                if v in root:
                    res_down = search(mat,m+1,n,root[v],v)
                    for r in res_down:
                        res.append(prefix+r)
                else:
                    assert v.upper() in root
                    res.append(prefix+v)

                    res_down = search(mat,m+1,n, root[v.upper()], v)
                    for r in res_down:
                        res.append(prefix+r)                   
                
                mat[m+1][n] = v
            # left
            if n>0 and mat[m][n-1] and (mat[m][n-1] in root or mat[m][n-1].upper() in root):
                v = mat[m][n-1]
                mat[m][n-1] = None
                
                if v in root:
                    res_left = search(mat, m, n-1, root[v], v)
                    for r in res_left:
                        res.append(prefix+r)
                else:
                    res.append(prefix+v)
                    res_down = search(mat,m,n-1, root[v.upper()], v)
                    for r in res_down:
                        res.append(prefix+r) 
                
                mat[m][n-1] = v
            # right
            if n+1< N and mat[m][n+1] and (mat[m][n+1] in root or mat[m][n+1].upper() in root):
                v = mat[m][n+1]
                mat[m][n+1] = None
                
                if v in root:
                    res_right = search(mat, m, n+1, root[v], v)
                    for r in res_right:
                        res.append(prefix+r)
                else:
                    res.append(prefix+v)
                    res_right = search(mat, m, n+1, root[v.upper()], v)
                    for r in res_right:
                        res.append(prefix+r)                    
                
                mat[m][n+1] = v
            return res

        res = []
        for m in range(M):
            for n in range(N):
                if (board[m][n] in tie_tree or board[m][n].upper() in tie_tree):
                    # BFS
                    v = board[m][n]
                    board[m][n] = None
                    if v in tie_tree:
                        for r in search(board, m, n, tie_tree[v], v):
                            res.append(r)
                    else: # v.upper() in tie_tree
                        res.append(v)
                        for r in search(board, m, n, tie_tree[v.upper()], v):
                            res.append(r)
                    board[m][n] = v
                else:
                    pass
        
        res = list(set(res))
        res.sort()
        return res

"""
[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
["oath","pea","eat","rain"]
[["a","a"]]
["a"]
[["a","b"],["c","d"]]
["ab","cb","ad","bd","ac","ca","da","bc","db","adcb","dabc","abb","acb"]
"""
