class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        turns = ((0, 1), (0, -1), (1, 0), (-1, 0))
        def dfs(x, y):
            if not (0 <= x < len(grid) and 0 <= y < len(grid[0])) or grid[x][y] == '0':
                return
            grid[x][y] = '0'
            for turn in turns:
                dfs(x+turn[0], y+turn[1])
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count
