"""
Given an array nums and a target value k, find the maximum length of 
a subarray that sums to k. If there isn’t one, return 0 instead. Note: 
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.
"""

def maxSubArrayLen(nums, k):
    """
    Time complexity: O(n)
    Strategy: keep track of running sum and map sums to its index. Each iteration, check
    if running_sum - k (I'll call it prev_running_sum) is in the dictionary. If it 
    does, the subarray from prev_running_sum index to the current index has a sum of k.
    """
    res, running_sum, sum_to_idx = 0, 0, {0: -1}
    for i, x in enumerate(nums):
        running_sum += x
        if running_sum not in sum_to_idx:
            sum_to_idx[running_sum] = i
        if running_sum - k in sum_to_idx:
            res = max(res, i - sum_to_idx[running_sum - k])
    return res

def test():
    assert(maxSubArrayLen([1, -1, 5, -2, 3], 3)) == 4
    assert(maxSubArrayLen([-2, -1, 2, 1], 1)) == 2
    return 'tests pass'

print(test())