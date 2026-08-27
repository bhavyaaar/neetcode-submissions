class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums)+1)]
        freq = {}
        for n in nums:
            freq[n] = freq.get(n,0) + 1 
        for num, count in freq.items():
            buckets[count].append(num)

        result = []
        for i in range(len(buckets) - 1, 0, -1): #iterats through the index
            for num in buckets[i]: #this is needed because there coulc be multiple numbers at index i in buckets [3,4], so the the for loop will iterate through that
                result.append(num)
                if len(result) == k:
                    return result
        


            



      


        