class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sumA = sum(A)
        sumB = sum(B)
        diff = (sumA - sumB)/2
        A = set(A)
        B = set(B)
        for a in A:
            if (a - diff) in B: 
                return [a, int(a-diff)]
