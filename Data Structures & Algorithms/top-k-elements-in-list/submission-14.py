class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #gonna create buckets essentially where the index is the frequency and the list is the value 

        buckets = [[] for _ in range( len(nums) + 1 )]

        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        for n,v in freq.items():
            buckets[v].append(n)

        result = []
        for r in range(len(buckets) -1 , 0, -1):
            for num in buckets[r]: 
                result.append(num)
        
            if len(result) == k:
                return result


    

        




        