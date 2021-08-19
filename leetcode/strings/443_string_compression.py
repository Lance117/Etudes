class Solution:
    def compress(self, chars: List[str]) -> int:
        i = write_idx = 0
        while i < len(chars):
            chars[write_idx] = chars[i]
            write_idx += 1
            j = i
            while j < len(chars) and chars[j] == chars[i]:
                j += 1
            count = j - i
            if count > 1:
                count_s = str(count)
                for c in count_s:
                    chars[write_idx] = c
                    write_idx += 1
            i = j
        return write_idx
