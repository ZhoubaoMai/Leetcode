class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        increase = True
        decrease = True
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                increase = False
            elif A[i] < A[i+1]:
                decrease = False
            if decrease == False and increase == False:
                return False
        return True
