class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        cache = [[0] * (N + 1) for _ in range(K + 1)]
        m = 0
        while cache[K][m] < N:
            m += 1
            for k in range(1, K + 1):
                cache[k][m] = cache[k][m - 1] + cache[k - 1][m - 1] + 1
        return m
