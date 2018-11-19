class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        value = list()
        value.append(nums[0])
        maxValue = nums[0]
        for i in range(1, len(nums)):
            if nums[i] ==1:
                value.append(value[i-1]+1)
            else:
                if maxValue < value[i-1]:
                    maxValue = value[i-1]
                value.append(0)
        if maxValue < value[-1]:
            return value[-1]
        return maxValue
