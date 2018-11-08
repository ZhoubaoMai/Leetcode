class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1.DP   longest(i) = longest(i-1) + 1 ,if nums[i] >nums[i-1]
        #                     1, otherwise
        # if len(nums) ==0:
        #     return 0
        # longest=[0 for i in range(len(nums))]
        # longest[0] = 1
        # for i in range(1, len(nums)):
        #     if nums[i] > nums[i-1]:
        #         longest[i] = longest[i-1] +1
        #     else:
        #         longest[i] = 1
        # return max(longest)
        
#         2. without memory
        longest = 1
        currentLong = 1
        if len(nums) == 0:
            return 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                currentLong += 1
                longest = max(longest, currentLong)
            else:                
                currentLong = 1
        return longest
