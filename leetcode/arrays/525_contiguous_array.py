"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Time complexity: O(n)
Same strategy as maximum sum subarray, but with a target of 0. Set each '0' to -1 so that we know
there are an equal number of 0s and 1s when the subarray sum is 0.
"""

def findMaxLength(nums):
    d = {0: -1}
    res = running_sum = 0
    for i, x in enumerate(nums):
        running_sum += x
        if running_sum in d:
            res = max(res, i - d[running_sum])
        else:
            d[running_sum] = i
    return res