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
    divisor, dp = 1**9 + 7, [1] * len(S)
    for i, c in enumerate(S):
        for j in range(i):
            dp[i] = (dp[i] + dp[j]) % divisor
    return sum(dp) % divisor