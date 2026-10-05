class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #max amount of buckets that can be there are the amount of numbers in nums
        buckets = [[] for _ in range(len(nums) + 1)]
        #buckets is [[],[],[]]

        freqnum = {}
        for num in nums:
            freqnum[num] = freqnum.get(num, 0) + 1

        for i, val in freqnum.items():
            buckets[val].append(i) 

        result = []
        for i in range(len(buckets)-1, -1, -1):
            for value in buckets[i]:
                result.append(value)
                if len(result) == k:
                    return result




        
        