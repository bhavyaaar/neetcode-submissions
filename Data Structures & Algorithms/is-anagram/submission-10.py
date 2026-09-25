class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqs = {}
        freqt = {}

        for ch in s:
            freqs[ch] = freqs.get(ch, 0) + 1
        for chh in t:
            freqt[chh] = freqt.get(chh, 0) + 1


        if freqs == freqt:
            return True 
        else:
            return False
        