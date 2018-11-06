import itertools
class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        rows = len(nums)
        columns = len(nums[0])
        if rows * columns != r*c:
            return nums
        else:
            nums = list(itertools.chain.from_iterable(nums))
            return [nums[i:i+c] for i in range(0, rows*columns, c)]
