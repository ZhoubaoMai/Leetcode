class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

#       1. binary search
        # start = 0
        # end = len(nums)-1
        # while start<=end:
        #     mid = int((start + end)/2)
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] > target:
        #         end = mid-1      # remeber to minus 1 !!!!!!!
        #     else:
        #         start = mid+1
        # return start
        
        # 2. find position of the cloest number of target in the array
        for index,num in enumerate(nums):
            if num>=target:
                return index
        return len(nums)

