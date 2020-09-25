class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                top = matrix[i][j]
                matrix[i][j] = matrix[~j][i]
                matrix[~j][i] = matrix[~i][~j]
                matrix[~i][~j] = matrix[j][~i]
                matrix[j][~i] = top
