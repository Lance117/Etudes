from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = list(Counter(tasks).values())
        max_n = max(counts)
        max_c = counts.count(max_n)
        slots = (n - max_c + 1) * (max_n - 1)
        idle = max(0, slots - (len(tasks) - max_n * max_c))
        return len(tasks) + idle
