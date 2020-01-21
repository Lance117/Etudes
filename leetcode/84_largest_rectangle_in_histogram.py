"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Problem link: https://leetcode.com/problems/largest-rectangle-in-histogram/description/
"""

def largest_rectangle_area_1:
    """
    Nested loop strategy: go through each bar width possibility, setting the
    shortest rectangle's height as the height for calculating area. The result
    is the highest area value.

    Note: this works, but times out on leetcode. Time complexity: O(n^2).
    """
    largest_area = 0
    for i in range(len(heights)):
        h = heights[i]
        for j in range(i, len(heights)):
            h = min(h, heights[j])
            largest_area = max(largest_area, h * (j - i + 1))
    return largest_area
