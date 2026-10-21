class Solution:
    def isPalindrome(self, s: str) -> bool:

        # alphanumeric characters, function in python called .isalnum -> returns a boolean value that can be TRUE/FALSE
        # two pointers iterating through 
        # lower the string completely 

        s = s.lower()
        l = 0 
        r = len(s) - 1
        
        while r > l:
            while r > l and not s[l].isalnum():
                l += 1 
            while r > l and not s[r].isalnum():
                r -= 1
            if s[r] != s[l]:
                return False
            r -= 1
            l += 1
        return True


        