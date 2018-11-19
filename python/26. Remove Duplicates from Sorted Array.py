class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # two pointer
        # one pointer to select the current number, another pointer to point the duplicate numbers to the current number
        # if len(nums) == 0:
        #     return 0
        # current = 0
        # for i in range(1, len(nums)):
        #     if nums[current] != nums[i]:
        #         current += 1
        #         nums[current] = nums[i]
        # return current+1
    
        # another two pointer way
        current = 0
        for num in nums:
            # print("current number: {}".format(num))
            # print("before: {}, current: {}".format(nums, current))
            if current <1 or num > nums[current-1]:
                nums[current] = num
                current += 1
            # print("after: {}, current: {}".format(nums, current))
        return current
