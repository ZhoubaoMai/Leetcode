from collections import Counter
class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#       1. first solution (time limit exceed)  
        # count = dict()
        # for num in nums:
        #     if num in count.keys():
        #         count[num] += 1
        #     else:
        #         count[num] = 1
        # maxNums = [k for (k, v) in count.items() if v == max(count.values())]
        # minsub = list()
        # for maxNum in maxNums:
        #     index = [i for i,v in enumerate(nums) if v == maxNum]
        #     if len(index) == 1:
        #         minsub.append(0)
        #     else:
        #         sub = index[-1] - index[0]
        #         minsub.append(sub)
        # return min(minsub)+1
    
#       2. reduce the loop !!!! If things can be done in one loop, do not use more
        first = dict()
        last = dict()
        count = dict()
        for index, num in enumerate(nums):
            if num in count.keys():
                count[num] += 1
                last[num] = index
            else:
                count[num] = 1
                first[num] = index
                last[num] = index
        maxCount = max(count.values())
        sub = [last[num] - first[num] + 1 for num, values in count.items() if values == maxCount]
        return min(sub)
