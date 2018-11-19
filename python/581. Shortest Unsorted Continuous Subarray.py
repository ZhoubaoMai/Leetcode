class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#        1.use sorting
        if len(nums) == 1:
            return 0
        asc = sorted(nums)
        first, last = 0, len(nums)-1
        while first < len(nums) and nums[first] == asc[first]:
            first += 1
        while last > first and nums[last] == asc[last]:
            last -= 1
        return last - first +1
    
#       2. two pass  
#       property: 1. if i,j is the bound, then:  nums[:i] and nums[j:] are in ascending order; 
#                 2. nums[i-1] <= min(nums[i:j]) and nums[j+1] >= max(nums[i:j])
#                 3. nums[i] != sortednums[i] and nums[j] != sortednums[j]
#       the reason of property 2: suppose the sorted array of nums[i:j] is sortNums, sortNums[0] 
#       should be the minium value in nums[i:j] and srtNums[-1] is the max.
#       if nums[i-1] > sortNums[0] or nums[j+1] < sortNums[-1], the whole array still not in ascending order


        i,j = 0, len(nums)-1
        while i<len(nums)-1 and nums[i] <= nums[i+1]:
            i += 1
        if i == len(nums)-1:
            return 0
        while j>i and nums[j] >= nums[j-1]:
            j -= 1
        
        subMax = nums[i]
        subMin = nums[i]
        for index in range(i,j+1):
            if subMax < nums[index]:
                subMax = nums[index]
            if subMin > nums[index]:
                subMin = nums[index]
        
        while i >=1 and nums[i-1] > subMin:
            i -= 1
        while j <len(nums)-1 and nums[j+1] < subMax:
            j += 1
        return j-i+1
        
        # 3. one pass:   from the property mentioned in two pass, we know
        # nums[i-1] <= min(nums[i:j]) and nums[j+1] >= max(nums[i:j])
#         therefore, we can find the bound i,j by find the smallest index i that nums[i] != min(nums[i+1:]); j is the biggest index that nums[j] != max(nums[:j-1])
        
        subMax=nums[0]
        subMin=nums[-1]
        i, j = 0, -1
        last = len(nums)-1
        for first in range(len(nums)):
            if nums[first] > subMax:
                subMax = nums[first]
            if subMax != nums[first]:
                j = first
            if nums[last] < subMin:
                subMin = nums[last]
            if subMin != nums[last]:
                i = last
            last -= 1
        return j -i +1
