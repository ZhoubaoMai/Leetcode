class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # 1. brute force (time limit exceed)
        # if not nums:
        #     return 0
        # sumSub = []
        # sumSub.append(nums[0])
        # for i in range(1, len(nums)):
        #     sumSub.append(sumSub[i-1] + nums[i])
        # minSub = math.inf
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         subarray = sumSub[j] - sumSub[i] + nums[i]
        #         if subarray >= s:
        #             minSub = min(minSub, j-i+1)
        #             break
        # return 0 if minSub == math.inf else minSub
    
        # 2. binary search
        # since subarray = sumSub[j] - sumSub[i] + nums[i] and subarray >= s
        # we know sumSub is an ascending array, so we can apply binary search to find the
        # sumSub[j] that sumSub[j] >= s+sumSub[i]-num[i]
        # if not nums:
        #     return 0
        # sumSub = []
        # sumSub.append(nums[0])
        # minSub = math.inf
        # for i in range(1, len(nums)):
        #     sumSub.append(sumSub[i-1] + nums[i])
        # for i in range(len(nums)):
        #     # binary search             
        #     start = i
        #     end = len(nums) - 1
        #     while start <= end:
        #         mid = (start+end) //2
        #         if sumSub[mid] >= s+sumSub[i]-nums[i]:
        #             end = mid -1
        #         else:
        #             start = mid + 1
        #     if start < len(nums):
        #         minSub = min(minSub, start - i +1)
        # return 0 if minSub == math.inf else minSub
        
        # 3. two pointer
        if not nums:
            return 0
        left, sumSub, minSub = 0, 0, math.inf
        for i in range(len(nums)):
            sumSub += nums[0]
            while (sumSub >= s):
                minSub = min(minSub, i-left+1)
                sumSub -= nums[left]
                left += 1
        return 0 if minSub == math.inf else minSub
        
