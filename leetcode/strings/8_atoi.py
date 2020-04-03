"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is 
found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical
digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no 
effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists 
because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Only the space character ' ' is considered as whitespace character.

note: answer in range of [-2^31, 2^31 - 1]
"""

def myAtoi(str):
    INT_MAX, INT_MIN = 2**31 - 1, -2**31
    res, s = 0, str.lstrip()
    if not (s and s[0] in list('+-0123456789')):
        return res
    sign = -1 if s[0] == '-' else 1
    for c in s[not s[0].isnumeric():]:
        if not c.isnumeric():
            break
        res = res * 10 + int(c)
        if res > (2**31 if sign < 0 else 2**31 - 1):
            return INT_MIN if sign < 0 else INT_MAX
    return sign * res