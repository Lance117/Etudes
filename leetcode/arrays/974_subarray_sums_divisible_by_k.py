"""
Given an array A of integers, return the number of (contiguous, non-empty) subarrays
that have a sum divisible by K.

Time and space complexity: O(n)
Use dictionary to keep track of remainders from prefix_sum / K. Goal is a remainder of 0,
so if the remainder_sum was from a previous subarray, ignoring that subarray would leave us
with a subarray sum divisible by K.
"""

def subarraysDivByK(A, K):
    d = {0: 1}
    count = remainder_sum = 0
    for n in A:
        remainder_sum = (remainder_sum + n) % K
        count += d.get(remainder_sum, 0)
        d[remainder_sum] = d.get(remainder_sum, 0) + 1
    return count