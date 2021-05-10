class NumArray:

    def __init__(self, nums: List[int]):
        self._sums = [0] + nums[:]
        for i in range(1, len(self._sums)):
            self._sums[i] += self._sums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        return self._sums[right + 1] - self._sums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
