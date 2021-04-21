class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums.reverse()
        self.rev_range(nums, 0, k - 1)
        self.rev_range(nums, k, len(nums) - 1)
        return nums
    
    def rev_range(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1
