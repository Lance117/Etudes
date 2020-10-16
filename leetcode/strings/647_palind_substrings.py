class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0       
        for i in range(len(s)):
            for j in (i, i + 1):
                l, r = i, j
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    res, l, r = res + 1, l - 1, r + 1
        return res
