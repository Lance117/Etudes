class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        if mod ele is allowed
        """
        if not matrix:
            return []
        res = []
        SHIFT = ((0, 1), (1, 0), (0, -1), (-1, 0))
        m, n = len(matrix), len(matrix[0])
        x = y = direction = 0
        for i in range(m * n):
            res.append(matrix[x][y])
            matrix[x][y] = 0
            next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
            if not 0 <= next_x < m  or not 0 <= next_y < n or matrix[next_x][next_y] == 0:
                direction = (direction + 1) & 3
                next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
            x, y = next_x, next_y
        return res

    def spiralOrder2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        mod ele not allowed
        """
        res = []
        if not matrix or not matrix[0]:
            return res
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        dir = "right"
        while top <= bottom and left <= right:
            if dir is "right":
                for i in range(left, right + 1):
                    res.append(matrix[top][i])
                dir, top = "down", top + 1
            elif dir is "down":
                for i in range(top, bottom + 1):
                    res.append(matrix[i][right])
                dir, right = "left", right - 1
            elif dir is "left":
                for i in reversed(range(left, right + 1)):
                    res.append(matrix[bottom][i])
                dir, bottom = "up", bottom - 1
            elif dir is "up":
                for i in reversed(range(top, bottom + 1)):
                    res.append(matrix[i][left])
                dir, left = "right", left + 1
        return res
