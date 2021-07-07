class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        N = len(board)
        cols = [set()  for _ in range(N)]
        rows = [set() for _ in range(N)]
        grids = [set() for _ in range(N)]

        for i in range(N):
            for j in range(N):
                if board[i][j] == '.':
                    board[i][j] = 0
                else:
                    board[i][j] = int(board[i][j])
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    grids[(i//3)*3+j//3].add(board[i][j])

        def _solveSudoku(board) -> bool: 
            for i in range(N):
                for j in range(N):
                    if board[i][j] == 0:
                        for x in range(1,10):
                            if x in rows[i] or x in cols[j] or x in grids[(i//3)*3+j//3]:
                                continue
                            
                            board[i][j] = x
                            rows[i].add(x)
                            cols[j].add(x)
                            grids[(i//3)*3+j//3].add(x)

                            if _solveSudoku(board):
                                return True
                            else:
                                rows[i].remove(x)
                                cols[j].remove(x)
                                grids[(i//3)*3+j//3].remove(x)

                        board[i][j] = 0    
                        return False                                           
                    else:
                        pass
            return True
        
        _solveSudoku(board)
        for i in range(N):
            for j in range(N):
                board[i][j] = str(board[i][j])

        return 
