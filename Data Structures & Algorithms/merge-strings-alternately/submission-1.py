class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # create a new result array
        # two pointers approach where we can iterate through each and append to the new result array 

        result = ""
        i = 0
        j = 0
        while i < len(word1) and j < len(word2):
            result += word1[i]
            result += word2[j]
            i += 1
            j += 1
        result += word1[i:]
        result += word2[j:]
        return result
            


        