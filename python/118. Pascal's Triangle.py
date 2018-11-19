class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        tri = [[1]]
        if numRows <= 1:
            return tri
        for i in range(1,numRows):
            row = list()
            for j in range(i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(tri[i-1][j-1] + tri[i-1][j])
            tri.append(row)
        return tri
