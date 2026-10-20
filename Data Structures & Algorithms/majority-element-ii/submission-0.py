class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        output = []
        freq = {} 
        for n in nums:
            freq[n] = freq.get(n,0) + 1
        
        for i in freq:
            if freq[i] > len(nums) // 3:
                output.append(i)
        return output

        