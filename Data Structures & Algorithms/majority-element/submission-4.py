class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #to find this i think i wil have to keep track of the frequency of a number and the actual number
        #majority means that it will occur the most 

        maj = nums[0]
        maxCount = 0
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            
            if freq[num] > maxCount:
                maxCount = freq[num]
                maj = num
                
        return maj






        
        