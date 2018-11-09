import math
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
#        1. use the property of Pascal's triangle (the jth element in ith row = C(j,i) = (i)! / ((j)! * (i-j)!) ) index starts from 0
        # return [int(math.factorial(rowIndex)/(math.factorial(i)*math.factorial(rowIndex-i))) for i in range(rowIndex+1)]

#       2. build a Pascal's triangle and return the kth row
        # tri = [[1],[1,1]]
        # for i in range(2, rowIndex+1):
        #     row = [tri[i-1][j] + tri[i-1][j-1] if 0<j<i else 1 for j in range(i+1)]
        #     tri.append(row)
        # return tri[rowIndex]

#       3. using zip:  
#       make two copys of the current row( row1 = row + [0]; row2 = [0] + row) 
#       the next row is the sum of each elements in the row.         
        row = [1]
        for i in range(rowIndex):
            row = [x+y for x,y in zip(row+[0], [0]+row)]
        return row
