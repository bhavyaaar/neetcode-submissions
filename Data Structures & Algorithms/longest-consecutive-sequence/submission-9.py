class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #keep track of longest sequence and current number and find out if that certain number you are at is the starting seqeunce by chekcign if the number below o

        numset = set(nums)
        longest = 0 
        for num in nums:
            if num - 1 not in numset:  
                length = 1

                while num + length in numset:
                    length += 1
                    
                longest = max(length , longest)

        return longest 
                    

                
        


            

        