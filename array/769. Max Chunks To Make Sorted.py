class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        # 1.
#         item = 0
#         visited = set()
#         rest = len(nums)
#         for index,num in enumerate(arr):
#             if num == item:
#                 rest = rest -index -1
#             else:
#                 if num in visited:
#                     rest -= 1
#             visited.add(num)
        
        # 2. brute force   if the maxmium of the sub array is equal to the index, then we can put them 
        # into a chunk and sort them
        ans, maxSub = 0, 0
        for i, x in enumerate(arr):
            maxSub = max(maxSub, x)
            if maxSub == i: 
                ans += 1
        return ans
                
    
                
            
