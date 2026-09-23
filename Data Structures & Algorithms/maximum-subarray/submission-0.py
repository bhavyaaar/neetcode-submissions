class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #kadane's algorithm is used:
            # at every nums[i] we want to figure out if extending the subarray forward would increase the running sum we have or decrease it 
            # if it wouldn't then we stop it and start a new subarray 
            # keep a global sum and a current sum to compare how the sum at each point 
            #if it ever goes to negative we need to account for that and just turn thte subarray to 0

            globalsum = nums[0]
            currentsum =  0


            for num in nums:
                #if the current running sum is less than 0 
                if currentsum < 0:
                    currentsum = 0   #
                currentsum = currentsum + num
                globalsum = max(currentsum, globalsum)

            return globalsum




            

                    
         



        