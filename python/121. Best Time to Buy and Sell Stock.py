class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
# #         1.brute search(time limit exceed)
#         maxProfit = 0
#         for i in range(0,len(prices)-1):
#             for j in range(i+1, len(prices)):
#                 maxProfit = max(maxProfit, prices[j] - prices[i])        
#         return maxProfit

        # 2. one pass
#       the max profit of a sub array is the difference between the min value and the max value comes after it
        
        minPrice = math.inf
        maxProfit = 0
        for price in prices:
            if price <= minPrice:
                minPrice = price
            else:
                maxProfit = max(price-minPrice, maxProfit)
        return maxProfit
