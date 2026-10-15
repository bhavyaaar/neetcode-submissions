class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        # s must be shorter than t
        if len(s) > len(t):
            return False

        # two pointers, one initialized on string s, and the other at t
        i = 0
        l = 0


        while i < len(s) and l < len(t):
            if s[i] == t[l]:
                i += 1
            l += 1   #run all of l   
        #this means we found every character in s             
        if i == len(s):
            return True
        return False
     
        






        
        