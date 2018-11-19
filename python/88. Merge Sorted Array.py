class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        
        # 1. two pointer
        # m -= 1
        # n -= 1
        # index=len(nums1)-1
        # if n < 0:
        #     return
        # while m >= 0 and n >= 0:
        #     if nums1[m] > nums2[n]:
        #         nums1[m], nums1[index] = nums1[index], nums1[m]
        #         m -= 1
        #     else:
        #         nums2[n], nums1[index] = nums1[index], nums2[n]
        #         n -= 1
        #     index -= 1
        # for i in range(n+1):
        #     nums1[i], nums2[i] = nums2[i], nums1[i]
        
        # 2.in place sorting
        nums1[m:] = nums2
        nums1.sort()
