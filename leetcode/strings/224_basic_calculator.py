class Solution:
    def calculate(self, s: str) -> int:
        def subcalc(s_lst):
            stk = []
            num = 0
            sign = '+'
            while len(s_lst) > 0:
                c = s_lst.pop()
                if c.isdigit():
                    num = num * 10 + int(c)
                if c == '(':
                    num = subcalc(s_lst)
                if (not c.isdigit() and c != ' ') or len(s_lst) == 0:
                    if sign == '+':
                        stk.append(num)
                    elif sign == '-':
                        stk.append(-num)
                    elif sign == '*':
                        stk[-1] *= num
                    elif sign == '/':
                        stk[-1] /= num
                    num, sign = 0, c
                if c == ')':
                    break
            return sum(stk)    
        
        return subcalc(list(s)[::-1])
        
