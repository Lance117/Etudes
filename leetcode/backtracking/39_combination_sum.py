class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def comboHelper(subset, start, total):
            if total == target:
                result.append(list(subset))
                return
            for i in range(start, len(candidates)):
                c = candidates[i]
                if total + c > target:
                    return
                subset.append(c)
                comboHelper(subset, i, total + c)
                subset.pop()
                
        candidates.sort()
        result = []
        comboHelper([], 0, 0)
        return result
