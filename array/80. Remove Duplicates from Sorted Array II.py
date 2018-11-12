class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       # two pointer similar to I
        # if len(nums) == 0:
        #     return 0
        # current = 0
        # mostTwo = False
        # for i in range(1, len(nums)):
        #     # print('{}th iteration'.format(i))
        #     # print("before: {}, current: {}, mostTwo: {}".format(nums, current, mostTwo))
        #     if nums[current] != nums[i]:
        #         current += 1
        #         nums[current] = nums[i]
        #         mostTwo = False
        #     else:
        #         if mostTwo == False:
        #             current += 1
        #             nums[current] = nums[i]
        #             mostTwo = True
        #     # print("after: {}, current: {}, mostTwo: {}".format(nums, current, mostTwo))
        # return current+1
        
        # improvement of 1
        current = 0
        for num in nums:
            # print("current number: {}".format(num))
            # print("before: {}, current: {}".format(nums, current))
            if current <2 or num > nums[current-2]:
                nums[current] = num
                current += 1
            # print("after: {}, current: {}".format(nums, current))
        return current
