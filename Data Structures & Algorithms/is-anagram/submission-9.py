class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        freq1 = {}
        freq2 = {}

        for i in s:
            freq1[i] = freq1.get(i, 0) + 1

        for c in t:
            freq2[c] = freq2.get(c, 0) + 1

        
        if freq1 == freq2:
            return True
        else:
            return False

        #time complexity: O(n) + O() = O(n)
        #space compelxity: since two frequency hashmaps were 
        #O(n)


        