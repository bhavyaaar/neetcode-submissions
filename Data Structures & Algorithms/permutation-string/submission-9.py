class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False


        counts1 = [0] * 26 
        counts2 = [0] * 26

        for c in s1:
            counts1[ord(c) - ord('a')] += 1

        for c in range(len(s1)):
            counts2[ord(s2[c]) - ord('a')] += 1
        
        if counts1 == counts2:
            return True
        

        l = 0 
        for r in range(len(s1), len(s2)):
            counts2[ord(s2[r]) - ord('a')] += 1 #adds the new letter 
            counts2[ord(s2[r - len(s1)])- ord('a') ] -= 1 # i want to take out the letter from the left side 
            
            if counts1 == counts2:
                return True
        return False

            
        

        
        