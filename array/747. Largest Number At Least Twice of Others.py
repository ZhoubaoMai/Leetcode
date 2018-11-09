class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#        1.sort
        if len(nums) == 1:
            return 0
        sortNums = sorted(nums)
        if sortNums[-1] >= 2*sortNums[-2]:
            return nums.index(sortNums[-1])
        else:
            return -1
        
#       2.loop once to find the biggest the second biggest number
#         if len(nums) == 1:
#             return 0
#         firBig, secBig = -math.inf, -math.inf
#         firIndex = -1
#         for index, num in enumerate(nums):
#             if num > firBig:
#                 firBig, secBig, firIndex = num, firBig, index
#             elif num > secBig:
#                 secBig = num
        
#         if firBig >= 2*secBig:
#             return firIndex
#         else:
#             return -1
