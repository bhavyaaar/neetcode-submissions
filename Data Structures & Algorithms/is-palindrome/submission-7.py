class Solution:
    def isPalindrome(self, s: str) -> bool:

        #case sensitive -> should turn the letters all lower case
        # to check for alphanuemric characters -> .isalnum
        # ignore any non, so skip past them simply 
        s = s.lower() 

        #two pointers that start at opposite ends 

        l = 0 
        r = len(s) - 1

        while l < r:
            while l < r and not s[r].isalnum():
                r -= 1
            while l < r and not s[l].isalnum():
                l += 1
            if s[l] != s[r]:
                return False
            r -= 1
            l += 1
        return True
        