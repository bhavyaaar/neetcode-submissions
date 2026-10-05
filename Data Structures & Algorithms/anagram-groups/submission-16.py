class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #anagram is two words exact same characters means we care about the frequency of each character 

        
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26 
 
            for ch in s:
                
                count[ord(ch) - ord('a')] += 1

            result[tuple(count)].append(s)

        return list(result.values())


        

        
        