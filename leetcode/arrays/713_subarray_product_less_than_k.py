"""
You are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all 
the elements in the subarray is less than k.

Time complexity: O(n). Sliding window to keep track of subarrays, and a variable
to keep track of the subarray product. Since this is an array of positive ints,
everything within a good subarray also counts.
"""

def numSubarrayProductLessThanK(nums, k):
    count = start = 0
    prod = 1
    for end in range(len(nums)):
        prod *= nums[end]
        while start < end and prod >= k:
            prod, start = prod / nums[start], start + 1
        if prod < k:
            count += (end - start + 1)
    return count
