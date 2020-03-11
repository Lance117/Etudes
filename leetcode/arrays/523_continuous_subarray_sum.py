"""
Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous
subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.

O(n) time and space complexity. Use hashmap to store remainders from prefix sum and k. If that remainder exists
from a previous subarray and the length is greater than 1, then it meets the requirements and we return True.

Edge case: mod by 0 error, so only get the remainder if k isn't 0.
"""

def checkSubarraySum(nums, k):
    d, prefix_remainder = {0: -1}, 0
    for i, x in enumerate(nums):
        prefix_remainder += x
        if k:
            prefix_remainder %= k
        if prefix_remainder in d and (i - d[prefix_remainder] > 1):
            return True
        if prefix_remainder not in d:
            d[prefix_remainder] = i
    return False