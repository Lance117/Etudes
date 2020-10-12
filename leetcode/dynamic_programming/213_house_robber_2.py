class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(l, r):
            n_2 = n_1 = 0
            for i in range(l, r):
                n_2, n_1 = n_1, max(n_1, nums[i] + n_2)
            return n_1
        return nums[0] if len(nums) < 2 else max(helper(0, len(nums) - 1), helper(1, len(nums)))
