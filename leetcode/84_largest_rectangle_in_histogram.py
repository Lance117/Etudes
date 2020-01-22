"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Problem link: https://leetcode.com/problems/largest-rectangle-in-histogram/description/
"""

def largest_rectangle_area_slow:
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

def largest_rectangle_area_fast:
    """
    We can improve on the first solution by cutting the number of times we
    iterate the 'heights' input. The optimization idea uses the fact that
    rectangles are surrounded by shorter bars or the start and end of the
    array. The strategy is to keep track of elements by storing the index in an
    array (that way we can keep track of where an observed rectangle starts and
    ends, as well as keep track of the heights). Then when we encounter a value
    that ends a rectangle, we can look in the stack and work backwards from
    there.

    Time complexity: O(n) because it passes array items at most twice.
    Space complexity: O(n) - space used increases linearly with size of input.
    """
    largest_area, prev_encountered = 0, []
    for i, end in enumerate(heights + [0]):
        while prev_encountered and heights[prev_encountered[-1]] >= end:
            height = heights[prev_encountered.pop()]
            width = i if not prev_encountered else i - prev_encountered[-1] - 1
            largest_area = max(largest_area, height * width)
        prev_encountered.append(i)
    return largest_area
    
