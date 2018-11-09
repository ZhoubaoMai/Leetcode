class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#         1. DP with memory    maxSum(i) = maxSum(i-1) > 0? maxSum(i-1)+nums(i) : nums(i)
        # maxSum = [None for i in range(len(nums))]
        # maxSum[0] = nums[0]
        # for i in range(1, len(nums)):
        #     if maxSum[i-1] > 0:
        #         maxSum[i] = maxSum[i-1] + nums[i]
        #     else:
        #         maxSum[i] = nums[i]
        # return max(maxSum)

      # 2. DP without memory
        maxSum = nums[0]
        curSum = nums[0]
        for i in range(1, len(nums)):
            if curSum > 0:
                curSum += nums[i]
            else:
                curSum = nums[i]
            maxSum = max(curSum, maxSum)
        return maxSum
        
        # 3. divide and conquer    maxSubarray = max(maxSubarray(lefthalf), maxSubarray(righthalf), maxSubarray(array cross the mid point))
        # if len(nums) == 1:
        #     return nums[0]
        # mid = int(len(nums)/2)
        # lmidMax, rmidMax = nums[mid], nums[mid]
        # tempSum = nums[mid]
        # for i in range(mid-1, -1, -1):
        #     tempSum += nums[i] 
        #     lmidMax = max(lmidMax, tempSum)
        # tempSum = nums[mid]
        # for i in range(mid+1,len(nums)):
        #     tempSum += nums[i]  
        #     rmidMax = max(rmidMax, tempSum)
        # return max(self.maxSubArray(nums[:mid]), self.maxSubArray(nums[mid:]), lmidMax+rmidMax-nums[mid])
