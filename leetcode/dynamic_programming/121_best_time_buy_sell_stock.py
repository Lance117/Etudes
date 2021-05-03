class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = float('-inf')
        buy = float('inf')
        for p in prices:
            buy = min(p, buy)
            res = max(res, p - buy)
        return res
