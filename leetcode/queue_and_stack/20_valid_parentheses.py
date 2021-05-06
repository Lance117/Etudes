class Solution:
    def isValid(self, s: str) -> bool:
        b_map = {')':'(', '}':'{', ']':'['}
        stk = []
        for c in s:
            if c not in b_map:
                stk.append(c)
            else:
                if not stk or b_map[c] != stk[-1]:
                    return False
                stk.pop()
        return len(stk) == 0
