class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list)

        for s in strs:
            freq = {}

            for c in s:
                freq[c] = freq.get(c, 0) + 1

            key = tuple(sorted(freq.items())) 
            result[key].append(s)

        return list(result.values())
            
        #time comeplexity is O(n*k) if there are n words and there are k letters in each word then it would be O(n*k)
        #space complexity wouldnt be crazy because 
    


                
                
            

        