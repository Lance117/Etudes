class Solution:
    def reverse(self, x: int) -> int:
        LIM = 2**31
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        res = 0
        while x:
            res = res * 10 + x % 10
            if res > LIM - (1 if sign == 1 else 0):
                return 0
            x //= 10
        return sign * res
