class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for interval in intervals:
            if newInterval[0] < interval[0]:
                interval, newInterval = newInterval, interval
            if res and interval[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
        if res and newInterval[0] <= res[-1][1]:
            res[-1][1] = max(res[-1][1], newInterval[1])
        else:
            res.append(newInterval)
        return res
