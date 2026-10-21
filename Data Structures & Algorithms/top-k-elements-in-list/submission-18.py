class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        # bucket sort 

        buckets = [[] for _ in range(len(nums) + 1)]

        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        # {"1:8","2:7"}

        for i, val in freq.items():
            buckets[val].append(i)
            #[[2,3],[6]]

        output = []
        for b in range(len(buckets) - 1, 0, -1):
            for num in buckets[b]:
                output.append(num)
                if len(output) == k:
                    return output

            






        