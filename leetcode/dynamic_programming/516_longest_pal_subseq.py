class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        cache = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            cache[i][i] = 1
        for i in reversed(range(len(s) - 1)):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    cache[i][j] = cache[i + 1][j - 1] + 2
                else:
                    cache[i][j] = max(cache[i][j - 1], cache[i + 1][j])
        return cache[0][len(s) - 1]
