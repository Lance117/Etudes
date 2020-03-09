"""
Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

If there is no non-empty subarray with sum at least K, return -1.

Time and space complexity: O(N)
Solution uses monotonic queue to keep track of read indices, and an array to keep track
of prefix sums. Two pointer sliding window technique doesn't work because of negative and
zero values. The queue stores indices in increasing order value so that a sliding window
works.
"""

from collections import deque

def shortestSubarray(A, K):
    prefix_sums = [0] * (len(A) + 1)
    for i in range(1, len(prefix_sums)):
        prefix_sums[i] = p[i - 1] + A[i - 1]
    res, q = len(A) + 1, deque()
    for i, x in enumerate(prefix_sums):
        while q and x <= prefix_sums[q[-1]]:
            q.pop()
        while q and x - p[q[0]] >= K:
            res = min(res, i - q.popleft())
    q.append(i)
    return res if res <= len(A) else -1