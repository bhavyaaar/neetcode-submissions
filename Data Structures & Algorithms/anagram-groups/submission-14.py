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
            
    


                
                
            

        