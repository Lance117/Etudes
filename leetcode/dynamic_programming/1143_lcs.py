class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        cache = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    cache[i][j] = 1 + cache[i - 1][j - 1]
                else:
                    cache[i][j] = max(cache[i - 1][j], cache[i][j - 1])
        return cache[-1][-1]

    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        cache = {}
        def dp(i, j):
            if i < 0 or j < 0:
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            if text1[i] == text2[j]:
                return dp(i - 1, j - 1) + 1
            res = max(dp(i - 1, j), dp(i, j - 1))
            cache[(i, j)] = res
            return res
        return dp(len(text1) - 1, len(text2) - 1)
