class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 1. backtrack
#         res = [[]]
#         # nums.sort()
#         def backtrack(subset, index):
#             for i in range(index, len(nums)):
#                 res.append(subset + [nums[i]])
#                 backtrack(subset + [nums[i]], i+1)
#         backtrack([], 0)
#         return res
        
        # 2. bit manipulation
        # For example, if there are three numbers in the array, the number of subsets will be eight. Choosing which number goes to which subset is like flipping bits. There are three numbers so I have three bits 0 0 0. The 0th subset has nothing. The first subset only has the first number 0 0 1. The second subset only has the second number 0 1 0... The 7th subset has all three numbers 1 1 1.
        res = []        
        for i in range(2 ** len(nums)):
            mask = 1
            subset = []
            for j in range(len(nums)):
                if(i & mask != 0):
                    subset.append(nums[j])                
                mask = mask << 1            
            res.append(subset)
        return res
