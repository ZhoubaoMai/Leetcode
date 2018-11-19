from collections import Counter
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#         idea 1: use python counter
        # count = Counter(nums)
        # return max(count, key = count.get)
        
#         idea 2: if there exists a majority element, then it must be the [n/2]th element in the sorted array
        nums = sorted(nums)
        return nums[int(len(nums)/2)]
