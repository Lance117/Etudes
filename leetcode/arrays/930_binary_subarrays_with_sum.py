"""
In an array A of 0s and 1s, how many non-empty subarrays have sum S?
"""

def numSubarraysWithSum(A, S):
    """
    time and space complexity: O(n). Hashmap stores prefix sums and keeps
    count each time it occurs.
    """
    d = {0: 1}
    count = running_sum = 0
    for x in A:
        running_sum += x
        if running_sum - S in d:
            count += d[running_sum - S]
        d[running_sum] = d.get(running_sum, 0) + 1
    return count