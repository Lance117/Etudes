class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        placement = [0] * n
        
        def backtrack(row):
            if row == n:
                res.append(placement[:])
                return
            for col in range(n):
                if isValid(row, col):
                    placement[row] = col
                    backtrack(row + 1)
                    placement[row] = 0
                               
        def isValid(row, col):
            for r, c in enumerate(placement[:row]):
                if abs(col - c) in (0, row - r):
                    return False
            return True
                    
        backtrack(0)
        for i in range(len(res)):
            p = res[i]
            strRow = ['.' * col + 'Q' + '.' * (n - col - 1) for col in p]
            res[i] = strRow
        return res
