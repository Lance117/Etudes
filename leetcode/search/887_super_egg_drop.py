class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        cache = {}
        def eggDrop(K, N):
            # base cases
            if K == 1:
                return N
            if N == 0:
                return 0
            # check cache
            if (K, N) in cache:
                return cache[(K, N)]
            res = float('inf')
            lo, hi = 1, N
            # binary search
            while lo <= hi:
                mid = (lo + hi) // 2
                broken = eggDrop(K - 1, mid - 1)
                not_broken = eggDrop(K, N - mid)
                if broken > not_broken:
                    hi, res = mid - 1, min(res, broken + 1)
                else:
                    lo, res = mid + 1, min(res, not_broken + 1)
            # store res in cache
            cache[(K, N)] = res
            return res
        return eggDrop(K, N)
