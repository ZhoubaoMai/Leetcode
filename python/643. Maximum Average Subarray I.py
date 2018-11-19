class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # 1. DP  sumK(i) = sumK(i-1) -nums[i-1] + nums[i-1+k]
        # sumK=list()
        # sumK.append(sum(nums[:k]))
        # for i in range(1, len(nums)-k+1):
        #     sumK.append(sumK[i-1]-nums[i-1]+nums[i-1+k])
        # return max(sumK)/k
        
        # 2. without memory
        preK = sum(nums[:k])
        maxK = preK
        for i in range(1, len(nums)-k+1):
            curK = preK-nums[i-1]+nums[i-1+k]
            if curK > maxK:
                maxK = curK
            # maxK = max(curK, maxK)   if is faster than max function
            preK = curK
        return maxK/k
        
            
