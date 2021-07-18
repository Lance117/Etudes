from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        j = len(s1)
        if not (s1 and s2) or len(s1) > len(s2):
            return False
        s1d = Counter(s1)
        while j <= len(s2):
            start = i
            s2d = {}
            while start < j:
                c = s2[start]
                if c not in s1d:
                    break
                s2d[c] = s2d.get(c, 0) + 1
                start += 1
            if s1d == s2d:
                return True
            i += 1
            j = i + len(s1)
        return False
