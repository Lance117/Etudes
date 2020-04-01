"""
Given a string s, find the longest palindromic substring in s. 
You may assume that the maximum length of s is 1000.

My solution: for each character with and without its neighbor, start with this
substring. Keep expanding until the substring is no longer a palindrome.

time complexity: O(n^2)
space: O(1)
"""

def longestPalindrome(s):
    def expand(i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i, j = i - 1, j + 1
        return (i + 1, j)
    
    res = (0, 0)
    for i in range(len(s)):
        for j in (i, i + 1):
            substr = expand(i, j)
            res = max(res, substr, key=lambda x: x[1]-x[0])
    return s[res[0]:res[1]]