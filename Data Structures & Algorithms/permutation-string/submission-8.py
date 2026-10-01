class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #check if string 1 is greater than s2 bc if it is then there can't be a permutation substring in the smaller string 
        if len(s1) > len(s2):
            return False

        #creating s1 and s2 frequency array, s1 gets the full and s2 is the frist window
        s1count = [0] * 26
        s2count = [0] * 26

        for s in range(len(s1)):
            s1count[ord(s1[s]) - ord('a')] += 1
            s2count[ord(s2[s]) - ord('a')] += 1

        if s1count == s2count:
            return True 
        l = 0
        for r in range(len(s1), len(s2)):
            s2count[ord(s2[r]) - ord('a')] += 1 # adds the new character 
            s2count[ord(s2[r - len(s1)]) - ord('a')] -= 1 # take out the new character

            if s1count == s2count:
                return True
        
        return False


        

        

            



             
   




        