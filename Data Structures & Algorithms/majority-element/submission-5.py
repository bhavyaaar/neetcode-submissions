class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        maj = nums[0] #the candidate for being the result
        maxCount = 0 # the maxCount is like the largest amoutn we have seen so far

        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
            if freq[num] > maxCount:
                maxCount = freq[num] #if we see a greater maxCount value
                maj = num #change to the number

        return maj



        