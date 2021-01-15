class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        digits, res = [0] * (m + n), ''
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                prod = int(num1[i]) * int(num2[j])
                idx1, idx2 = i + j, i + j + 1
                combined = digits[idx2] + prod
                digits[idx2] = combined % 10
                digits[idx1] += combined // 10
        i = 0
        while i < len(digits) and digits[i] == 0:
            i += 1
        for idx in range(i, len(digits)):
            res += str(digits[idx])
        return '0' if len(res) == 0 else res
