class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = rep_n = 0
        count = {}
        for i, c in enumerate(s):
            count[c] = count.get(c, 0) + 1
            rep_n = max(rep_n, count[c])
            if res - rep_n < k:
                res += 1
            else:
                count[s[i - res]] -= 1
        return res
