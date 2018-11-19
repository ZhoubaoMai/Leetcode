class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1. use counter (Do not meet the requirement O(1) extra space )
        # from collections import Counter
        # count = Counter(nums)
        # return max(count, key=count.get)
        
        # 2.sort (do not meet the requirement)
        
        # nums= sorted(nums)
        # for i in range(1,len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return nums[i]
        
        # 3. use binary search and pigeonhole principle  start =1, end= len(nums)-1,
        # mid= (start+end)//2.  If the number in nums greater mid is greater than mid
        # (say if the mid is 100 (so the array contains 201 numbers), 
        # and there are 101 numbers in the array greater than 100.
        # Since each number in the array is between 1 and 200, so there are 101 numbers in the
        #  range [101, 200]; According to the pigeonhole principle, there must have a duplicate   
        # in [101, 200], so we search the right half of the array by change start=mid)
        # if len(nums) == 0:
        #     return 0
        # start = 1
        # end = len(nums)-1
        # while start < end:
        #     mid = (start + end) //2
        #     count = 0
        #     for num in nums:
        #         if num <= mid:
        #             count += 1
        #     if count > mid:
        #         end = mid
        #     else:
        #         start = mid+1
        # return end
        
        # 4. cycle detection
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                break
        return slow
    
        
