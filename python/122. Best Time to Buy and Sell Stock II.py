class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
# it will be better if it clarify we can buy one and sell one in the same day in the problem description 
        maxProfit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                maxProfit = maxProfit + prices[i] - prices[i-1]
        return maxProfit
