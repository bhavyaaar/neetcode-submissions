class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if len(s) > len(t):
            return False

        i = 0
        l = 0
        while i < len(s) and l < len(t):
            if s[i] == t[l]:
                i += 1
            l += 1
        if i == len(s):
            return True
        return False 
        
        
            


        