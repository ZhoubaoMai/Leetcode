class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 1. backtracking
        def backtrack(index, path, candidates, target,res):
            if target == 0:
                res.append(path)
                return
            else:
                for i in range(index, len(candidates)):
                    if candidates[i] > target:
                        break
                    backtrack(i, path+[candidates[i]], candidates, target-candidates[i],res)
        res = []
        candidates.sort()
        backtrack(0, [], candidates, target,res)
        return res
        
        # 2.improvement of 1
        # res = []
        # candidates.sort()
        # def backtrack(path, candidates, target):
        #     if target == 0:
        #         res.append(path)
        #         return
        #     else:
        #         for num in candidates:
        #             if num > target:
        #                 break
        #             elif not path or num >= path[-1]:
        #                 backtrack(path+[num], candidates, target-num)
        # backtrack([], candidates, target)
        # return res
