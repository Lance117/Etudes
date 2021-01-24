class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(perm):
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            for num in nums:
                if num not in perm:
                    perm.append(num)
                    backtrack(perm)
                    perm.pop()              
        
        res = []
        backtrack([])
        return res
