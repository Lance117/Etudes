class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        dead, live, die, res = range(4)
        
        def count(row, col):
            count = 0
            turns = ((1, 0), (-1, 0), (0, 1), (0, -1),
                     (1, 1), (-1, -1), (-1, 1), (1, -1))
            for turn in turns:
                nRow, nCol = row + turn[0], col + turn[1]
                if 0 <= nRow < m and 0 <= nCol < n:
                    if board[nRow][nCol] in (live, die):
                        count += 1
            return count
            
        for i in range(m):
            for j in range(n):
                c = count(i, j) # implement later
                if board[i][j] in (live, die):
                    if c < 2 or c > 3:
                        board[i][j] = die
                else:
                    if c == 3:
                        board[i][j] = res
        for i in range(m):
            for j in range(n):
                if board[i][j] == die:
                    board[i][j] = dead
                elif board[i][j] == res:
                    board[i][j] = live
