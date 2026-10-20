class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        maj = nums[0]
        maxCount = 0
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        for i in freq:
            if freq[i] > maxCount:
                maxCount = freq[i]
                maj = i
        return maj

        