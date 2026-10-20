class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """


        #requires the swapping algorithm and two pointers approach 

        l = 0 
        r = len(s) - 1

        while r > l:
            s[l], s[r] = s[r], s[l]
            r -= 1
            l += 1
        return s
        