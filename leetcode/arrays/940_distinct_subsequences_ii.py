"""
Given a string S, count the number of distinct, non-empty subsequences of S .

Since the result may be large, return the answer modulo 10^9 + 7.
"""

def distinctSubseqIIa(S):
    """
    O(n^2) time complexity, O(n) space. Times out on leetcode.
    
    Use dynamic programming to keep count
    of subsequences with that character. Char count would then be dp[i-1]+1,
    and the result is the sum of the counts.
    """
    divisor, dp = 10**9 + 7, [1] * len(S)
    for i, c in enumerate(S):
        for j in range(i):
            dp[i] = (dp[i] + dp[j]) % divisor
    return sum(dp) % divisor

def distinctSubseqIIb(S):
    """
    Instead of using an inner nested loop to keep track of subsequence count to
    an index, keep track of all subsequences on each iteration and cache the
    results for the current character. Recurrence relation: dp[k] = 2*dp[k-1] - cache[c]
    """
    res, cache = 1, {}
    for c in S:
        prev = res
        res = res * 2 - cache.get(c, 0) # total doubled to add subseq count with current char
        # subtract count from cache to not double count subsequences with current char
        cache[c] = prev # store subseq count up to this char
    return (res - 1) % (10**9 + 7) # - 1 to exclude count of empty string