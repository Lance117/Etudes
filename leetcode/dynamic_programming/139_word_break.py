class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        tab = [True] + [False] * len(s)
        for i in range(len(s)):
            if tab[i]:
                for j in range(i, len(s)):
                    if s[i:j+1] in words:
                        tab[j+1] = True
        return tab[-1]
