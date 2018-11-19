class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 1. backtracking
        # res = [[]]
        # nums.sort()
        # def backtrack(subset, index):
        #     for i in range(index, len(nums)):
        #         if i == index or nums[i] != nums[i-1]:
        #             res.append(subset + [nums[i]])
        #             backtrack(subset + [nums[i]], i+1)
        # backtrack([], 0)
        # return res
    
        # 2. iteration
        # if nums[i] is same to nums[i - 1], then it needn't to be added to all of the subset, just add it to the last l subsets which are created by adding nums[i - 1]
        res = [[]]
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [nums[i]])
        return res
        
