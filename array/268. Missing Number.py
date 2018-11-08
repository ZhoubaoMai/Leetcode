class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#       1. the same way as findDisappearedNumbers  
        # for index,num in enumerate(nums):
        #     if num < len(nums):
        #         i = int(num)
        #         nums[i] = float(nums[i])
        # for index,num in enumerate(nums):
        #     if type(num) is not float:
        #         return index
        # return len(nums)

        # 2. use sum
        # length = len(nums)
        # trueSum = int(length * (length+1)/2)
        # return trueSum - sum(nums)
        
        # 3. xor  (异或运算  A xor A =0)
        # result = 0
        # for i in range(len(nums)+1):
        #     result = result ^ i
        # for num in nums:
        #     result = result ^ num
        # return result
        
        # 4. binary search
        nums = sorted(nums)
        left = 0
        right = len(nums) - 1 
        while(left <= right):
            mid = int((left+right)/2)
            if(nums[mid] > mid):
                right -= 1
            else:
                left += 1
        return left
        
        
