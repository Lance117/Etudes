class Solution:
    class Trie:
        class Node:
            def __init__(self):
                self.children = [None] * 26
                self.is_end = False
        
        def __init__(self):
            self.root = self.Node()
            
        def insert(self, word):
            cur = self.root
            for c in word:
                i = ord(c) - ord('a')
                if not cur.children[i]:
                    cur.children[i] = self.Node()
                cur = cur.children[i]
            cur.is_end = True
                
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        st = self.Trie()
        res = []
        for word in words:
            st.insert(word)
            
        def dfs(x, y, pre, cur):
            if cur.is_end:
                res.append(pre)
                cur.is_end = False
            if not (0 <= x < len(board) and 0 <= y < len(board[0])):
                return
            c = board[x][y]
            i = ord(c) - ord('a')
            if c == '#':
                return
            board[x][y] = '#'
            dirs = ((1,0), (0,1), (-1,0), (0,-1))
            if cur.children[i]:
                for d in dirs:
                    dfs(x+d[0], y+d[1], pre+c, cur.children[i])
            board[x][y] = c
            
        for i in range(len(board)):
            for j in range(len(board[i])):
                dfs(i, j, '', st.root)
        return res
