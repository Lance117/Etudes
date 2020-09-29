class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        n_2, n_1 = 1, 1
        for i in range(1, len(s)):
            count = 0
            if 0 < int(s[i]) < 10:
                count += n_1
            if 10 <= int(s[i-1:i+1]) <= 26:
                count += n_2
            n_2, n_1 = n_1, count
        return n_1
