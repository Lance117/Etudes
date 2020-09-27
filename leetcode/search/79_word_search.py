class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, idx):
            if idx == len(word):
                return True
            if not (0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == word[idx]):
                return False
            board[i][j] = ''
            if any(map(dfs, [i-1, i+1, i, i], [j, j, j-1, j+1], [idx+1]*4)):
                return True
            board[i][j] = word[idx]
            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if dfs(i, j, 0):
                    return True
        return False
