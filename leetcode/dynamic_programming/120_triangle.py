"""
Given a triangle, find the minimum path sum from top to bottom. 
Each step you may move to adjacent numbers on the row below.

For example, given the following triangle:
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
"""

def minimumTotal1(triangle):
    """
    This solution uses tabulation - uses min path sum of adjacent nums from previous
    row to build a table of min path sums.

    Complexity analysis - n is the number of rows in triangle
    Time complexity: O(n^2)
    Space complexity: n(n + 1) / 2 --> O(n^2)
    """
    t = [[0] * (i + 1) for i in range(len(triangle))]
    t[0][0] = triangle[0][0]
    for row in range(1, len(triangle)):
        for col in range(len(triangle[row])):
            if col == 0:
                t[row][col] = triangle[row - 1][col]
            elif col == len(triangle) - 1:
                t[row][col] = triangle[row - 1][col - 1]
            else:
                t[row][col] = min(triangle[row - 1][col - 1], triangle[row - 1][col])
    return min(t[-1])