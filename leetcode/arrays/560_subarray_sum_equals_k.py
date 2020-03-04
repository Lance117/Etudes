"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum
equals to k.
"""

def subarraySum(nums, k):
    """
    Time complexity: O(n), space: O(n)
    Use dictionary to keep track of prefix sums. If a previous prefix exists such that running_sum - prev = k,
    then count that subarray.
    """
    count = running_sum = 0
    sum_count = {0: 1}
    for num in nums:
        running_sum += num
        count += sum_count.get(running_sum - k, 0)
        sum_count[running_sum] = sum_count.get(running_sum, 0) + 1
    return count