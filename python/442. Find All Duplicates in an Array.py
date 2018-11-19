class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 1. set the exsits num to negative
        ans = []
        for index, num in enumerate(nums):
            if nums[abs(num)-1] < 0:
                ans.append(abs(num))
            else:
                nums[abs(num)-1] = -nums[abs(num)-1]
        return ans
    
        # 2. use set (use extra space)
        # ans = []
        # duplicate = set()
        # for num in nums:
        #     if num in duplicate:
        #         ans.append(num)
        #     else:
        #         duplicate.add(num)
        # return ans
