class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write_idx = 0
        z_count = 0
        for n in nums:
            if n == 0:
                z_count += 1
            else:
                nums[write_idx] = n
                write_idx += 1
        for i in range(len(nums) - z_count, len(nums)):
            nums[i] = 0
