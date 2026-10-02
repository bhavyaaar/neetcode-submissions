class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #using a set to determine membership of a certain character 
        

        #using two pointers to establish a window and adding new characters into the set and checking at each new character if we have seen it before 
        # if so, we have seen it before then we need to be  moving the right pointer to take out the character from our window 
        #but once you take it out of the window you need to take it out of the seen set as well 
        seen = set()
        l = 0
        r = 0
        longest = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
   
            seen.add(s[r])
            longest =  max(r - l + 1, longest)

        return longest


        