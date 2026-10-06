class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # nums has n integers in [0,n]
        # consecutive means num + 1 exists check up till n 
        numset = set(nums)  #take out duplicated
        n = len(nums) # the length of nums
        for i in range(n+1): #iterate through  [0,n]
            if i not in numset: #checks if that value is in numset or not 
                return i 
        





        