class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 1. check the furtherest path the current element can go
        furtherest = nums[0]
        for i in range(1, len(nums)):
            if furtherest == 0:
                return False
            furtherest -= 1
            furtherest = max(furtherest, nums[i]) 
        return True
