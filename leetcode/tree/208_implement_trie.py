class Trie:
    
    class Node:
        def __init__(self):
            self.next = [None] * 26
            self.is_end = False
                
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        trav = self.root
        for c in word:
            if not trav.next[ord(c)-ord('a')]:
                trav.next[ord(c)-ord('a')] = self.Node()
            trav = trav.next[ord(c)-ord('a')]
        trav.is_end = True
        
    def search_prefix(self, prefix):
        trav = self.root
        for c in prefix:
            if not trav.next[ord(c)-ord('a')]:
                return None
            trav = trav.next[ord(c)-ord('a')]
        return trav

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        trav = self.search_prefix(word)
        return trav is not None and trav.is_end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.search_prefix(prefix)
        return node is not None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
