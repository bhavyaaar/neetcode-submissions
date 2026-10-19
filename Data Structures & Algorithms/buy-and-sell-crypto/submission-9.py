class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = sell - buy 
        # sell price needs to be higher than buy at all times 
        #things we want to keep track is running max profit and the buy price 


        maxP = 0
        b = 0 
       
        for s in range(1, len(prices)):
            if prices[b] > prices[s]:
                b = s
            else:
                profit = prices[s] - prices[b]
                maxP = max(profit, maxP)
        return maxP
        