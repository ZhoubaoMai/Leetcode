class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1. two pointer(won't work!)
        # if len(nums) == 0 or len(nums) == 2:
        #     return -1
        # if len(nums) == 1:
        #     return 0
        # left = 0
        # leftSum = nums[0]
        # right = len(nums) -1
        # rightSum = nums[len(nums)-1]
        # while right-left > 2:
        #     diff = leftSum - rightSum
        #     if diff > 0:
        #         right -= 1
        #         rightSum += nums[right]
        #     elif diff < 0:
        #         left += 1
        #         leftSum += nums[left]
        #     else:
        #         left += 1
        #         leftSum += nums[left]
        #         right -= 1
        #         rightSum += nums[right]
        # if leftSum == rightSum and right-left == 2:
        #     return left+1
        # else:
        #     return -1
        
        # 2. brute force
        # if len(nums) == 0 or len(nums) == 2:
        #     return -1
        # if len(nums) == 1:
        #     return 0
        # total = list()
        # total.append(nums[0])
        # for i in range(1, len(nums)):
        #     total.append(total[i-1]+nums[i])
        # for i in range(len(nums)):
        #     if i == 0:
        #         left = 0
        #         right=total[-1]-total[i]
        #     else:
        #         left=total[i-1]
        #         right=total[-1]-total[i]
        #     if left == right:
        #         return i
        # return -1
        
        # 3. prefix sum
        leftSum = 0
        totalSum = sum(nums)
        for index, num in enumerate(nums):   # enumerate is faster than indexing
            rightSum = totalSum - leftSum - num
            if rightSum == leftSum:
                return index
            else:
                leftSum += num
        return -1
