class TrieNode:
    def __init__(self):
        self.children, self.is_end = [None] * 26, False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        ptr = self.root
        for c in word:
            c_idx = ord(c) - ord('a')
            if not ptr.children[c_idx]:
                ptr.children[c_idx] = TrieNode()
            ptr = ptr.children[c_idx]
        ptr.is_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def dfs(cur, i):
            if i == len(word):
                return True if cur.is_end else False
            c_idx = ord(word[i]) - ord('a')
            if word[i] == '.':
                return any([dfs(node, i + 1) for node in cur.children if node])
            if cur.children[c_idx]:
                return dfs(cur.children[c_idx], i + 1)
            return False
        
        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
