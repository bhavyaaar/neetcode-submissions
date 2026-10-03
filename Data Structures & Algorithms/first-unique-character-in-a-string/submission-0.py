class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for i, value in enumerate(s):
            if freq[value] == 1:
                return i
        return -1