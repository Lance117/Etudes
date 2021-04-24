class Solution:
    def firstUniqChar(self, s: str) -> int:
        repeats_idx = {}
        res = float('inf')
        for i, c in enumerate(s):
            if c in repeats_idx:
                repeats_idx[c] = float('inf')
            else:
                repeats_idx[c] = i
        for idx in repeats_idx.values():
            res = min(res, idx)
        return -1 if res == float('inf') else res
