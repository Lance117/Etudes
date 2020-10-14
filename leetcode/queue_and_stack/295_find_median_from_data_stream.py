import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap, self.max_heap = [], []
        
    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, num))
        if len(self.max_heap) > len(self.min_heap):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def findMedian(self):
        """
        :rtype: float
        """
        return (self.min_heap[0] - self.max_heap[0]) / 2 if len(self.min_heap) == len(self.max_heap) else float(self.min_heap[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
