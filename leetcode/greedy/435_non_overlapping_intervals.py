"""
Given a collection of intervals, find the minimum number of intervals you need to remove to 
make the rest of the intervals non-overlapping.

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.

Greedy algorithm:
1. Select interval with the earliest finishing time
2. Count following intervals that overlap with that interval
3. Once you encounter an interval that doesn't overlap, select the interval with the next earliest
finishing time.
"""

def erase_overlap_intervals(intervals):
    res, visited = 0, float('-inf')
    for interval in sorted(intervals, key=lambda x: x[1]):
        if interval[0] >= visited:
            visited = interval[1]
        else:
            res += 1
    return res