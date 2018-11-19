class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # 1. straight forward
        if not nums:
            return nums
        res = []
        start=end=nums[0]
        for i in range(1, len(nums)):
            if nums[i] == end+1:
                end = nums[i]
            else:
                if start == end:
                    res.append("{}".format(start))
                else:
                    res.append("{}->{}".format(start, end))
                start = end = nums[i]
        if start == end:
            res.append("{}".format(start))
        else:
            res.append("{}->{}".format(start, end))
        return res
