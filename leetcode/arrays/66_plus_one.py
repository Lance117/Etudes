class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        for i in reversed(range(len(digits)- 1)):
            if digits[i + 1] == 10:
                digits[i + 1] = 0
                digits[i] += 1
            else:
                break
        if digits[0] == 10:
            digits[0] = 1
            digits.append(0)
        return digits
