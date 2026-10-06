class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        #so we want move the zeros we have in an array but maintian the relative order, so in a way its like a remove in place 
        # we movw every non zero element to positon where 0 is 

        l = 0 
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        
        