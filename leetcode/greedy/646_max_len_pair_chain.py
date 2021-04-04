class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        y=float('-inf')
        res = 0
        for p in pairs:
            if p[0] > y:
                res += 1
                y = p[1]
        return res
