class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        sett = set(nums) 
        longest = 0
        for n in nums:
            value = n - 1 #crucial to remeber: check for the inital starting of sequences
            if value not in sett:
                length = 1
                while (n + length) in sett:
                    length += 1
                longest = max(length,longest)
        return longest

#space complexity would be a O(n) because a set was created 
#time complexity would be O(n)

            


        


        