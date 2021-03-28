class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        
        def matcher(i, j):
            res = False
            if (i, j) in cache:
                return cache[(i, j)]
            if j == len(p):
                return i == len(s)
            m = i < len(s) and p[j] in (s[i], '.')
            if j < len(p) - 1 and p[j + 1] == '*':
                # explore paths
                res = matcher(i, j + 2) or (m and matcher(i + 1, j))
            else:
                res = m and matcher(i + 1, j + 1)
            cache[(i, j)] = res
            return res
        
        return matcher(0, 0)
