class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
#         1.DP  minCost(i) = cost(i) + min(minCost(i-1),minCost(i-2))
        minCost = [0 for i in range(len(cost))]
        minCost[0]=cost[0]
        minCost[1]=cost[1]
        for i in range(2,len(cost)):
            minCost[i] = cost[i] + min(minCost[i-1], minCost[i-2])
        return min(minCost[-1], minCost[-2])
        
