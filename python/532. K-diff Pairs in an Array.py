class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 1. brute force (time limit exceeded)
        # count = set()
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if abs(nums[i]-nums[j]) == k:
        #             pair = (nums[i], nums[j]) if nums[i] < nums[j] else (nums[j], nums[i])
        #             count.add(pair)
        # return len(count)
    
#         2. better frute force, use set    time limit exceeded
        # if k == 0:
        #     from collections import Counter
        #     counts = Counter(nums)
        #     return len([1 for count in counts.values() if count >= 2])
        # else:
        #     count = set()
        #     nums = list(set(nums))
        #     for i in range(len(nums)):
        #         for j in range(i+1, len(nums)):
        #             if abs(nums[i]-nums[j]) == k:
        #                 pair = (nums[i], nums[j]) if nums[i] < nums[j] else (nums[j], nums[i])
        #                 count.add(pair)
        #     return len(count)
        
#        3. the same as two sum, use hash table
        # from collections import Counter
        # counts = Counter(nums)
        # res = 0
        # for num,count in counts.items():
        #     if (k==0 and count >=2) or (k>0 and num+k in counts):
        #         res += 1
        # return res
    
        # 4. combine 2,3
        if k == 0:
            from collections import Counter
            counts = Counter(nums)
            return len([1 for count in counts.values() if count >= 2])
        elif k>0:
            return len(set(nums).intersection({num + k for num in nums}))
        return 0
