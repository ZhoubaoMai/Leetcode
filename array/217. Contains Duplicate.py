class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        setNums = set(nums)
        if len(setNums) < len(nums):
            return True
        else:
            return False
