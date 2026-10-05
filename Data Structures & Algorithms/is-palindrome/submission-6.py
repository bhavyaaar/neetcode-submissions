class Solution:
    def isPalindrome(self, s: str) -> bool:

        #string is immutable so if i am makign changes to it i need to save it to a varible

        s = s.lower()
        l = 0 
        r = len(s) - 1

        #if you have pointers that are starting and opposite ends then you want to make sure they don't cross
        while l < r:
            # make sure that the letter is alphanumeric, if it is skip and move forward
            while l < r and not s[r].isalnum():
                r -= 1
            while l < r and not s[l].isalnum():
                l += 1
            #do ^ this above before you check because you can't check a non alpha numeric 
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True
                

        