class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        for arr in sorted(intervals, key=lambda x: x[0]):
            if len(res) > 0 and arr[0] <= res[-1][1]:
                res[-1][1] = max(arr[1], res[-1][1])
            else:
                res.append(arr)
        return res
