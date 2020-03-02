"""
Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Time complexity: O(n)
Use a start and end pointer to keep track of increasing subsequences. If it's no longer increasing, set the
start to the end.
"""

def findLengthOfLCIS(nums):
    start = res = 0
    for end in range(len(nums)):
        if end and nums[end] <= nums[end - 1]:
            start = end
        res = max(res, end - start + 1)
    return res