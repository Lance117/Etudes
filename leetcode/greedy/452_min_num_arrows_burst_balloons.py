class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        res = 0
        x_end = float('-inf')
        for p in points:
            if p[0] > x_end:
                res += 1
                x_end = p[1]
        return res
