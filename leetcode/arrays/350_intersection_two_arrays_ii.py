from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count_a, count_b = Counter(nums1), Counter(nums2)
        res = []
        for k,v in count_a.items():
            if k in count_b:
                res += [k]*min(v, count_b[k])
        return res
