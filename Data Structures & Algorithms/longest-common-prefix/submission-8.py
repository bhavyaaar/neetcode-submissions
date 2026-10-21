class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        #need to start with the first string and iterate through the characters comparing that position characters in the other words 
        #check if the word is too small then we return [:i]

        for i in range(len(strs[0])):
            for s in strs:
                if len(s) == i or strs[0][i] != s[i]:
                    return strs[0][:i]
        return strs[0]

        