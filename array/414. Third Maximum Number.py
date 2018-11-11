class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        max1, max2, max3 = -math.inf, -math.inf, -math.inf
        for num in nums:
            if num > max1:
                max1, max2, max3 = num, max1, max2
            elif num > max2:
                max1, max2, max3 = max1, num, max2
            elif num > max3:
                max1, max2, max3 = max1, max2, num
        if len(nums) < 3:
            return max1
        return max3
