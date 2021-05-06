class Solution:
    def romanToInt(self, s: str) -> int:
        c_map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        for i in reversed(range(len(s))):
            if i != len(s) - 1 and c_map[s[i]] < c_map[s[i + 1]]:
                res -= c_map[s[i]]
            else:
                res += c_map[s[i]]
        return res
