class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 1. pop and insert
        # for i in range(k):
        #     temp = nums.pop(-1)
        #     nums.insert(0,temp)
        
        # 2 reverse
        # if k >= len(nums):
        #     k = k % len(nums)
        # nums.reverse()
        # for i in range(int(k/2)):
        #     nums[i], nums[k-i-1] = nums[k-1-i], nums[i]
        # for i in range(int((len(nums)-k)/2)):
        #     nums[k+i], nums[len(nums)-1-i] = nums[len(nums)-1-i], nums[k+i]
        
        # 3. just set the value
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]
