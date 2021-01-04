from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res, window = [], {}
        l = r = match = 0 # window ptrs, and num of chars that meet req
        needs = Counter(p)
        while r < len(s):
            c = s[r]
            if c in needs:
                window[c] = window.get(c, 0) + 1 # add to window
                if window[c] == needs[c]: # num of c count meets req
                    match += 1
            r += 1
            while match == len(needs): # found a valid window
                if r - l == len(p): # window contains anagram
                    res.append(l)
                c = s[l]
                if c in window:
                    window[c] -= 1 # remove from window
                    if window[c] < needs[c]: # window no longer meets req
                        match -= 1
                l += 1
        return res
                
