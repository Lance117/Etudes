class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total, res = nums[0], [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = total
            total *= nums[i]
        total = nums[-1]
        for i in reversed(range(len(nums) - 1)):
            res[i] *= total
            total *= nums[i]
        return res
