class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxes = 0
        tot = 0
        for n in nums:
            if n == 1:
                tot += 1
            else:
                tot = 0
            maxes = max(tot,maxes)
        return maxes