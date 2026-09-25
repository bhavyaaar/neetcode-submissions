class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #questions to ask: what if duplicatesn of a number, would that count as 1 number or multiple 
        
        sett = set(nums)
        longest = 0 
        for num in sett:
            if (num - 1) not in sett: #this is rlly the important thing to remember 
                length = 1
                while (num + length) in sett:
                    length += 1
                longest = max(longest, length)
        return longest




        