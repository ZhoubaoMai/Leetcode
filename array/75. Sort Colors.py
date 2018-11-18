class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 1. sort
        # nums.sort()
        
        # 2.two pass count
        # num0 = num1 = num2 = 0
        # for index, num in enumerate(nums):
        #     if num == 0:    
        #         num0 += 1
        #     elif num == 1:
        #         num1 += 1
        #     else:
        #         num2 += 1
        # for i in range(len(nums)):
        #     if i < num0:
        #         nums[i] = 0
        #     elif i <num0+num1:
        #         nums[i] = 1
        #     else:
        #         nums[i] = 2
        
        # 3. one pass Dutch National Flag Algorithm
        left = index = 0
        right = len(nums) - 1
        while (index <= right):
            if nums[index] == 0:
                nums[index], nums[left] = nums[left], nums[index]
                index += 1
                left += 1
            elif nums[index] == 1:
                index += 1
            else:
                nums[index], nums[right] = nums[right], nums[index]
                right -= 1
