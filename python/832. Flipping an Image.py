class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(A)):
            row = A[i][::-1]
            row = [1-i for i in row]                                
            A[i] = row
        return A
            
