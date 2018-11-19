class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
#       the key idea is to mark the ith element negative if the array contains number i
#       iterate the array second time, if jth element is postive, then the number j is missing
        for i in range(len(nums)):            
            index = abs(nums[i]) - 1    # be aware to use absoluate value!!!  the ith element may be negative 
            if nums[index] > 0:
                nums[index] = -nums[index]
        anw = list()
        for i in range(len(nums)):
            if nums[i] > 0:
                anw.append(i+1)
        return anw
