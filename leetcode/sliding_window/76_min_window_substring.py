from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        2 pointers for window, keep track of the best window and how many
        chars encountered that are in t. move right ptr to get all candidate
        chars, then move left to shrink the window
        """
        if not (s and t) or len(s) < len(t):
            return ""
        
        l = r = t_chars_count = all_encountered = 0
        min_range, letter_map, t_count = (0, len(s)), {}, Counter(t)
            
        while r < len(s):
            it = s[r]
            if it in t_count:
                letter_map[it] = letter_map.get(it, 0) + 1
                if letter_map[it] <= t_count[it]:
                    t_chars_count += 1
            r += 1
            
            while t_chars_count == len(t):
                all_encountered = True
                min_range = min(min_range, (l, r), key=lambda xy: xy[1]-xy[0])
                l_char = s[l]
                if l_char in t_count:
                    letter_map[l_char] -= 1
                    if letter_map[l_char] < t_count[l_char]:
                        t_chars_count -= 1
                l += 1
                
        x, y = min_range
        return s[x:y] if all_encountered else ""
