import collections
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        bucket = [[] for _ in range(len(nums) + 1)]
        count = collections.Counter(nums)
        for key,v in count.items():
            bucket[v].append(key)
        l = [x for sub in bucket for x in sub]
        return l[::-1][:k]
