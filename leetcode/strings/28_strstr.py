class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        if needle == '':
            return 0
        i = 0
        while i <= len(haystack) - len(needle):
            if haystack[i] == needle[0]:
                j, k = i, 0
                while j < len(haystack) and k < len(needle) and haystack[j] == needle[k]:
                    j, k = j + 1, k + 1
                if k == len(needle):
                    return i
            i += 1
        return -1
