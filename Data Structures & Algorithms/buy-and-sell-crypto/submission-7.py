class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #choose a day to buy stock and then a differnt day in the future to sell it -> sell - buy = profit 
        #returm maximum profit, establish a profit variable that gets updated each time 
        #using two pointers for buy price and sell price 
        #but would i have to iterate thru every single value?
        # use this approach: we want to kep track of min price AND maxprofit

        #these are pointers
        buy = 0 
        sell = 1
        maxprofit = 0 

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                maxprofit = max(profit, maxprofit)
            else:
                buy = sell
            sell += 1
        return maxprofit

                


                

        