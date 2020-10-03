class Solution:
    def rob(self, nums: List[int]) -> int:
        n_2 = n_1 = 0
        for n in nums:
            n_2, n_1 = n_1, max(n_1, n + n_2)
        return n_1
