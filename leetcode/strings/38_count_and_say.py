class Solution:
    def countAndSay(self, n: int) -> str:
        """
        f(1) = '1'
        f(2) = nextNum(f(1))
        """
        def nextNum(s):
            cur, count = s[0], 0
            res = ''
            for c in s:
                if c == cur:
                    count += 1
                else:
                    res += (str(count) + cur)
                    cur, count = c, 1
            res += (str(count) + cur)
            return res
        
        res = '1'
        for i in range(n - 1):
            res = nextNum(res)
        return res
