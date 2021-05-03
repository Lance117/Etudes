class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = cur = float('-inf')
        for n in nums:
            cur = max(n, cur + n)
            res = max(res, cur)
        return res
