class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1. DFS
        visited = set()
        def DFS(i):
            S = 0
            while nums[i] not in visited:
                visited.add(nums[i])
                i = nums[i]
                S += 1
            return S        
        longS = 1
        if len(nums) == 0:
            return 0       
        for i in range(len(nums)):
            if nums[i] not in visited:
                temp = DFS(i)
                if temp > longS:
                    longS = temp
        return longS
    
        
        # 2. improved DFS, set the visited value to -1, and if the rest numbers is less than total number - longest k, break
        def DFS(i):
            S = 0
            while nums[i] >=0:
                nums[i] = -1
                i = nums[i]
                S += 1
            return S       
        longS = 1
        sumVisited = 0        
        if len(nums) == 0:
            return 0       
        for i in range(len(nums)):
            if nums[i] >= 0:
                temp = DFS(i)
                if temp > longS:
                    longS = temp
                sumVisited += temp
                if len(nums) - sumVisited < longS:
                    break
        return longS
        
            
