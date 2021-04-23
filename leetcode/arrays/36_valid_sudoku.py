class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        00 01 02 | 03 04 05
        10 11 12 | 13 14 15
        20 21 22 | 23 24 25
        """
        # validate rows and columns
        for i in range(len(board)):
            visited_row, visited_col = set(), set()
            for j in range(len(board[i])):
                row_val, col_val = board[i][j], board[j][i]
                if row_val in visited_row or col_val in visited_col:
                    return False
                if row_val != '.':
                    visited_row.add(row_val)
                if col_val != '.':
                    visited_col.add(col_val)
        # validate boxes
        for s_row in range(3):
            for s_col in range(3):
                visited = set()
                for row in range(s_row*3, s_row*3 + 3):
                    for col in range(s_col*3, s_col*3 + 3):
                        cur = board[row][col]
                        if cur in visited:
                            return False
                        if cur != '.':
                            visited.add(cur)
        return True
