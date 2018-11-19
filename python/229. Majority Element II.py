class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #  Boyer-Moore Majority Vote algorithm       
        most = len(nums) // 3
        if not nums:
            return []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for num in nums:   # to avoid candidate1 and 2 has the same value
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        return [n for n in (candidate1, candidate2) if nums.count(n) > most]

                
