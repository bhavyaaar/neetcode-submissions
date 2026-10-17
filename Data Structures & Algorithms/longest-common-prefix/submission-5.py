class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        #compare the first word characters to the rest of the words at each index
        #add it to an output string 
        #two things to check for in if a string is too short or if a character doesn't equal 

        for i in range(len(strs[0])):
            for s in strs: #this helps move across the rest of the strinfs
                if i == len(s) or s[i] != strs[0][i]:  #if the string is too short or some characters in the new string don't match with the old one 
                    return s[:i]
        return strs[0]
             

        