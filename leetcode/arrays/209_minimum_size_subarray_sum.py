"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of
which the sum ≥ s. If there isn't one, return 0 instead.
"""

def minSubArrayLen1(s, nums):
    """
    Time complexity: O(n). Uses sliding window to keep track of subarrays.
    """
    res = float('inf')
    start = running_sum = 0
    for end in range(len(nums)):
        running_sum += nums[end]
        while start < len(nums) and running_sum >= s:
            res = min(res, end - start + 1)
            running_sum, start = running_sum - nums[start], start + 1
    return 0 if res == float('inf') else res
