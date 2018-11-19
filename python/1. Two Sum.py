class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 1. brute force
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums [j] == target:
        #             return [i,j]
         
        # 2. two pass hash,  build a dictionary for num 
        # numIndex=dict()
        # for index, num in enumerate(nums):
        #     numIndex[num] = index
        # for index, num in enumerate(nums):
        #     complement = target - num
        #     if complement in numIndex and numIndex[complement] != index:
        #         return [index, numIndex[complement]]
        
        # 3. one pass hash
        numIndex = dict()
        for index, num in enumerate(nums):
            complement = target-num
            if complement in numIndex:
                return [numIndex[complement], index]
            else:
                numIndex[num] = index
