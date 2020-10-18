class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not (matrix and matrix[0]):
            return []
        nsew = ((1, 0), (-1, 0), (0, 1), (0, -1))
        m, n = len(matrix), len(matrix[0])
        p_visited, a_visited = set(), set()
        
        def dfs(x, y, visited):
            if (x, y) in visited:
                return
            visited.add((x, y))
            for dir in nsew:
                next_x, next_y = x + dir[0], y + dir[1]
                if 0 <= next_x < m and 0 <= next_y < n and matrix[next_x][next_y] >= matrix[x][y]:
                    dfs(next_x, next_y, visited)
                    
        for i in range(m):
            dfs(i, 0, p_visited)
            dfs(i, n - 1, a_visited)
        for j in range(n):
            dfs(0, j, p_visited)
            dfs(m - 1, j, a_visited)
        return list(p_visited & a_visited)
                    
