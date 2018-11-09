class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # two pointer
        # one pointer to select the current number, another pointer to point the duplicate numbers to the current number
        if len(nums) == 0:
            return 0
        current = 0
        for i in range(1, len(nums)):
            if nums[current] != nums[i]:
                current += 1
                nums[current] = nums[i]
        return current+1
