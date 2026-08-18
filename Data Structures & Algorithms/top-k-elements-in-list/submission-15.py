class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #frequency count -> hash map 
        # need to figure out the greatest -> so using buckets []

        #the buckets need to be as long as the array is + 1
        buckets = [[] for _ in range(len(nums) + 1)]
        

        freq = {}
        for n in nums:
            freq[n] = freq.get(n,0) + 1

        for v, m in freq.items():
            buckets[m].append(v)

            

        results = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                results.append(num) #go into the bucket for frequency i and look at each number inside it. incase some may have [3, 4] in a bucket 
            if len(results) == k:
                return results

        