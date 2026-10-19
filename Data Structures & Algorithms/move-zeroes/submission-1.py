class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        #left pointer that only moves when we see a non zero value and make a swap 
        #right pointer needed as well 

        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r],nums[l]
                l += 1
        return nums


        