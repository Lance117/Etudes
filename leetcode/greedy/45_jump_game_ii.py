class Solution:
    def jump(self, nums: List[int]) -> int:
        res = furthest = chk = 0
        for i in range(len(nums) - 1):
            furthest = max(furthest, i + nums[i])
            if i == chk:
                res += 1
                chk = furthest
        return res
