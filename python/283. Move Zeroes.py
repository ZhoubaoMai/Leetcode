class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # length = len(nums)
        # i = 0
        # while i < length :
        #     # print (nums, i, nums[i])
        #     if nums[i] == 0:
        #         del nums[i]
        #         nums.append(0)
        #         length -= 1
        #     else:
        #         i += 1
        
        
        zero = 0 # record the position of 0 element 
        for i in range(len(nums)):
            if nums[i] != 0:
                if zero != i:
                    nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
                    
