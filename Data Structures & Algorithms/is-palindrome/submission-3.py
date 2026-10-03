class Solution:
    def isPalindrome(self, s: str) -> bool:
        #case-insensitive 
        #ignores all non-alphanuemric characters
        #.isalnum 
        #strings are immutable so when you make changes it creates a NEW string that needs to be saved to a variable 
        lowers = s.lower()
        r = len(s) - 1
        l = 0

        while r > l:
            while r > l and not lowers[r].isalnum():
                r -= 1
            while r > l and not lowers[l].isalnum():
                l += 1
            if lowers[l] != lowers[r]:
                return False
            l += 1
            r -= 1
        return True

                