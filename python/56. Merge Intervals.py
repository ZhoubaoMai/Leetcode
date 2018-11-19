# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # 1. brute force
        if not intervals:
            return []
        intervals = sorted(intervals, key = lambda x: x.start)
        current = intervals[0]
        res = list()
        for i in range(1, len(intervals)):
            if intervals[i].start > current.end:
                res.append(current)
                current = intervals[i]
            else:
                start = current.start
                end = current.end if current.end >= intervals[i].end else intervals[i].end
                current = Interval(start, end)
        res.append(current)
        return res
        
