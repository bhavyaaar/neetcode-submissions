class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #need to figure out essentially how many times each number appears in the array 

        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
            #this would create: {1:1, 2:2, 3:3} 
        
        sorted_nums = sorted(freq, key=freq.get, reverse=True)
            #key think to remmeber sorted is a function not method
            #need to specficy freq and the freq.get is the values and reverse order

        return sorted_nums[:k]
        #everything uptill k ! 


        #T.C. might be greater becaue it is sorting unqiue numebrs 0(nlogn)
        #S.C the freq array can have O(n) 

        

        