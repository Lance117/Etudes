"""
Given a non-empty string s, you may delete at most one character. 
Judge whether you can make it a palindrome.

Time complexity: O(N) - start two pointers at beginning and end. If characters
don't match, 'delete' a character and check if it's a palindrome.
"""

def validPalindrome(s):
    def isPal(l, r):
        """Checks if substring in s between two pointers is a palindrome."""
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
    
    for i in range(len(s) // 2):
        j = len(s) - i - 1
        if s[i] != s[j]:
            return isPal(i, j - 1) or isPal(i + 1, j)
    return True
