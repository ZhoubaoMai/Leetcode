import copy 
class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 1. backtrack
        res = []
        candidates.sort()
        def backtrack(path, candidates, target):
            if target == 0:
                res.append(path)
                return
            else:
                added = set()
                for i in range(len(candidates)):
                    if candidates[i] > target:
                        break
                    if candidates[i] in added:
                        continue
                    # if (not path or candidates[i] >= path[-1]):
                    added.add(candidates[i])
                    if i == len(candidates) -1:
                        temp = []
                    else:
                        temp = candidates[i+1:]
                    backtrack(path+[candidates[i]], temp, target - candidates[i])
        backtrack([], candidates, target)
        return res
