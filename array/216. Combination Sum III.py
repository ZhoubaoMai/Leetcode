class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        # 1. backtrack
        res = []
        candidates = [i for i in range(1, 10)]
        def backtrack(path, candidates, k, n):
            if k==0 and n ==0:
                res.append(path)
                return
            elif k==0:
                return
            for i in range(len(candidates)):
                if candidates[i] > n:
                    break
                if i == len(candidates) - 1:
                    temp = []
                else:
                    temp = candidates[i+1:]
                backtrack(path + [candidates[i]], temp, k-1, n-candidates[i])
        backtrack([], candidates, k, n)
        return res
                
