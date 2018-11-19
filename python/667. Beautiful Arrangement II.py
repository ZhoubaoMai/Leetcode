class Solution:
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        # if k >= n:
        #     return
        # res = [i for i in range(n-k+1)]
        # for i in range(2, k+1):
        #     res.append(res[-1] + i)
        # return res
        
        # 1. put the last element into the ith ararry, and reverse the i+1th to the last
        # res = [i for i in range(1, n+1)]
        # for i in range(1, k):
        #     res[i:] = rse[:i-1:-1]
        # return res
    
        # 2. improvement of 1,  first construct an array of diiference is 1, then follow the order
        # [1, n, 2, n-1] to construct the rest.
        # Reason: the first part give us a distinct difference 1, if follow the second order, can give
        # us n-1 distinct difference number.            
        # Hence, we need to first construct a n-k-1 array which difference is all 1, and follow
        # [n-k+1, n, n-k+2, n-1 ...] can give us k distinct difference include 1. 
        # Therefore the total distinct difference is k
        
#         first construct a n-k-1 array:
        res = [i for i in range(1, n-k)]
    
#         construct the [n-k, n, n-k+1, n-1 ...] part, we can observe that the even index (index starts from 0) is n-k-(int)(index/2) and the odd index is n-(int(index/2))
        for i in range(k+1):
            if i %2 == 0:
                res.append(n - k+ i//2)
            else:
                res.append(n - i//2)        
        return res
        
            
            
