class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i, j = i - 1, j + 1
            return (i + 1, j)
        
        res = (0, 0)
        for i in range(len(s)):
            for j in (i, i + 1):
                sub = expand(i, j)
                res = max(res, sub, key=lambda x: x[1]-x[0])
        return s[res[0]:res[1]]
