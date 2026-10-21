class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for c in s:
            freq[c] = freq.get(c,0) + 1
        
        for i, value in enumerate(s):
            if freq[value] == 1:
                return i
        return -1

            