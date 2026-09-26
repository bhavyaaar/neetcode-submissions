class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window problem 
        # two pointers that are i and j which will iterate through the string, and add the letter to a set
        # a set membership is O(1) -> we j care ab if true or not 
        # i and j are slow fast pointers so i only moves undera conidtion and j always will
        # find length so j+1 - i?


        sett = set()
        i = 0
        max_length = 0

        for j in range(len(s)): # this does the j++ for us so no need 
            while s[j] in sett: 
                sett.remove(s[i]) # if u area removing duplicates then u have to remove them from the set as well 
                i += 1
          
            sett.add(s[j]) # just need to take care of adding to the sert 
            max_length = max(max_length, j-i+1)


        return max_length









        