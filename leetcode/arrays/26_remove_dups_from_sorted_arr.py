class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        rd([1,2,2,2,3]) -> [1,2,3]
        rd([1,2,2]) -> [1,2]
        """
        write_idx = 0
        for i in range(len(nums)):
            if i == len(nums) - 1 or nums[i] != nums[i + 1]:
                nums[write_idx] = nums[i]
                write_idx += 1
        return write_idx
