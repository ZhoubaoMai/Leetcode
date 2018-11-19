class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1. brute force(time limit exceed)       
        # maxPro = -math.inf
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         maxPro = max(maxPro, 0)
        #         continue
        #     else:
        #         temp = nums[i]
        #         maxPro = max(maxPro, temp)
        #         for j in range(i+1, len(nums)):
        #             temp *= nums[j]
        #             maxPro = max(maxPro, temp)
        # return maxPro
        
        # 2. DP
        maximum=big=small=nums[0]
        for n in nums[1:]:
            big, small=max(n, n*big, n*small), min(n, n*big, n*small)
            maximum=max(maximum, big)
        return maximum
