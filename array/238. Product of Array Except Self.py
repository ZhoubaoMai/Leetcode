class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 1. division method  (not meet the problem request)
        
        # pro = 1
        # hasZero = 0
        # for num in nums:
        #     if num != 0:
        #         pro *= num
        #     else:
        #         hasZero += 1
        # if hasZero > 1:
        #     return [0 for num in nums]
        # if hasZero == 1:
        #     return [0 if num != 0 else pro for num in nums ]
        # return [int(pro/num) for num in nums]
        
        # 2. divide the product into two part, the left product and right product
        # result[i] = left[i] * right[i]  where  left[i] = nums[0] * num[1] *... * 
        #  num[i-2]*nums[i-1], right[i] = nums[i+1] * nums[i+2] * ... * 
        #  * nums[len(nums)-2] * nums[len(nums)-1]
        
        lproduct, rproduct = [], []
        lproduct.append(1)
        rproduct.append(1)  # notice th rproduct is in reverse order
        j = len(nums)-1
        # print(nums, len(nums))
        for i in range(1, len(nums)):
            j -= 1
            # print(i, j)
            lproduct.append(lproduct[i-1] * nums[i-1])
            rproduct.append(rproduct[i-1] * nums[j+1])
        
        # print(lproduct, rproduct)
        return [lproduct[i] * rproduct[len(nums)-1-i] for i in range(len(nums))]
