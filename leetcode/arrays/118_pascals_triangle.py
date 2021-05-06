class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        res = [[1], [1,1]]
        for _ in range(numRows - 2):
            row = [1]
            prev = res[-1]
            for i in range(len(prev) - 1):
                row.append(prev[i] + prev[i + 1])
            row.append(1)
            res.append(row)
        return res
