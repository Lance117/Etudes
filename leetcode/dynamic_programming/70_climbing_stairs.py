class Solution:
    def climbStairs(self, n: int) -> int:
        """
        n = 3
        f(1) = 1, f(2) = 2
        f(3) = f(2) + f(1)
        """
        n_2, n_1 = 1, 2
        if n == 1: return 1
        if n == 2: return 2
        for _ in range(n - 2):
            n_2, n_1 = n_1, n_1 + n_2
        return n_1
