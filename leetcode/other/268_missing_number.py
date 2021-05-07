class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        lo, hi = float('inf'), float('-inf')
        total = 0
        for n in nums:
            if n < lo:
                lo = n
            if n > hi:
                hi = n
            total += n
        if lo != 0:
            return 0
        if hi != len(nums):
            return len(nums)
        geo_sum = (len(nums) * (1 + len(nums))) // 2
        return geo_sum - total
