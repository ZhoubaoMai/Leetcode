import math
class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        # 1. straightfoward way (terrible thinking !!!!!!!)
        # row = len(M)
        # column = len(M[0])
        # if row == 1 and column ==1:
        #     return M        
        # A = [[0]*len(M[0])]*len(M)
        # i, j = 0, 0
        # A[0][0] = math.floor((M[i][j] + M[i][j+1] +M[i+1][j] + M[i+1][j+1])/4)
        # i, j = 0, len(M[0])-1
        # A[i][j] = math.floor((M[i][j-1] + M[i+1][j-1] + M[i][j] + M[i+1][j])/4)
        # i, j = len(M)-1, 0
        # A[i][j] = math.floor((M[i-1][j] + M[i-1][j+1] + M[i][j] + M[i][j+1])/4)
        # i, j = len(M)-1, len(M[0])-1
        # A[i][j] = math.floor((M[i-1][j] + M[i-1][j-1] + M[i][j] + M[i][j-1])/4)
        # for i in range(1, len(M)-1):
        #     for j in range(1, len(M[0])-1):
        #         A[i][j] = math.floor((M[i-1][j-1] + M[i][j-1] + M[i+1][j-1] + M[i-1][j] + M[i][j] + M[i+1][j] + M[i-1][j+1] + M[i][j+1] + M[i+1][j+1])/9)
        # for j in range(1, len(M[0])-1):
        #     i = 0
        #     A[i][j] = math.floor((M[i][j-1] + M[i][j] + M[i][j+1] + M[i+1][j-1] + M[i+1][j] + M[i+1][j+1])/6)
        #     i = len(M) -1
        #     A[i][j] = math.floor((M[i][j-1] + M[i][j] + M[i][j+1] +M[i-1][j-1] + M[i-1][j] + M[i-1][j+1] )/6)
        # for i in range(1, len(M)-1):
        #     j = 0
        #     A[i][j] = math.floor((M[i-1][j] + M[i][j] + M[i+1][j] + M[i-1][j+1] + M[i][j+1] + M[i+1][j+1])/6)
        #     j = len(M[0]) -1
        #     A[i][j] = math.floor(((M[i-1][j-1] + M[i][j-1] + M[i+1][j-1] + M[i-1][j] + M[i][j] + M[i+1][j])/6))
        # return A
        
        # 2. compute neighbour
        row = len(M)
        column = len(M[0])
        # can NOT use this way to initiate a m*n matrix, this will make a shadow copy m*n times
        # A = [[0]*len(M[0])]*len(M)
        A = [[0 for j in range(column)] for i in range(row)]
        for i in range(row):
            for j in range(column):
                neighbour = [M[x][y] for x in (i-1, i, i+1) for y in (j-1, j, j+1) if 0<=x<=row-1 and 0<=y<=column-1]
                A[i][j] = math.floor(sum(neighbour)/len(neighbour))
        return A
        
        
