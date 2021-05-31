class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        cache = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    cache[j] = max(cache[j], cache[i] + 1)
        return max(cache)
