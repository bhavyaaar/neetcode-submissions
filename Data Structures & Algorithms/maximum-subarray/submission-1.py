class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #another way to write this 
        # !! key idea is at every index we want to check if adding this value to the running sum will make it bigger or not, and we do this by comparing the current value to the running sum when added
        globalsum = nums[0]
        currentsum = 0

        for num in nums:
            if currentsum < 0:
                currentsum = 0
            currentsum = max(currentsum + num, num) #if currentsum+ num is larger then we keep eexrtending 
            globalsum = max(currentsum, globalsum)
        return globalsum
        