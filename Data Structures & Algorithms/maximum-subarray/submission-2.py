class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        r = 0
        l = 0 
        currsum = 0

        for r in range(len(nums)):
            if currsum < 0:
                currsum = 0
                l = r
            currsum += nums[r]
            maxsum = max(maxsum, currsum)
        return maxsum
        