class Solution:
    class Trie:
        class Node:
            def __init__(self):
                self.next, self.is_end = [None] * 26, False
                
        def __init__(self):
            self.root = self.Node()
            
        def insert(self, word):
            trav = self.root
            for c in word:
                c_idx = ord(c) - ord('a')
                if not trav.next[c_idx]:
                    trav.next[c_idx] = self.Node()
                trav = trav.next[c_idx]
            trav.is_end = True
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(i, j, pre, curr):
            neighbors = ((i-1, j), (i+1, j), (i, j-1), (i, j+1))
            if curr.is_end:
                result.append(pre)
                curr.is_end = False
            if not (0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] != '#'):
                return
            cur_ch = board[i][j]
            c_idx = ord(cur_ch) - ord('a')
            board[i][j] = '#'
            if curr.next[c_idx]:
                for pos in neighbors:
                    dfs(pos[0], pos[1], pre+cur_ch, curr.next[c_idx])
            board[i][j] = cur_ch
        
        st, result = self.Trie(), []
        for word in words:
            st.insert(word)
        for i in range(len(board)):
            for j in range(len(board[i])):
                dfs(i, j, '', st.root)
        return result
        
