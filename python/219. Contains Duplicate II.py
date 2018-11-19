class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # # 1. brute force  compare if exists duplicate in ith element to i+kth element
        # if len(set(nums)) == len(nums):     # if all unique return false
        #     return False
        # if len(nums) <= k:
        #     k = len(nums) -1
        # for i in range(len(nums)):
        #     j = i+1
        #     while j <= i+k and j<len(nums):
        #         if nums[i] == nums[j]:
        #             return True
        #         j += 1
        # return False
        
        # 2.use a block to compare   
        # initialise block [0, 1, 2 ...k] check if exists duplicate numbers under the requirement,
        # loop the rest of the nums, for each loop, only need to compare block[1:] and nums[i]
        
        # if len(set(nums)) == len(nums):     # if all unique return false
        #     return False
        # if len(nums) <= k:
        #     k = len(nums) -1
        # block = nums[:k+1]
        # for i in range(len(block)):
        #     for j in range(i+1,len(block)):
        #         if block[i] == block[j]:
        #             return True
        # for i in range(k+1, len(nums)):
        #     block.pop(0)
        #     for num in block:
        #         if num == nums[i]:
        #             return True
        #     block.append(nums[i])
        # return False
        
        # 3. similar to TWO SUMS, use a hash table
        if len(set(nums)) == len(nums):     # if all unique return false
            return False
        duplicate = dict()
        for i,n in enumerate(nums):
            if n in duplicate and i - duplicate[n] <= k:
                return True
            else:
                duplicate[n] = i
        return False
