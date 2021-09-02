class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    # set 0' row
                    for k in range(n):
                        if matrix[i][k] != 0:
                            matrix[i][k] = '0'
                    # set 0' col
                    for k in range(m):
                        if matrix[k][j] != 0:
                            matrix[k][j] = '0'
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    matrix[i][j] = 0
