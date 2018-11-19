class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        def isMagic(a,b,c,d,e,f,g,h,i):
            corner=set([2,4,6,8])
            return set([a,c,g,i]) == corner and b+e+h == d+e+f == a+b+c ==15
        for i in range(1,len(grid)-1):
            for j in range(1, len(grid[0])-1):
                if grid[i][j] != 5:
                    continue
                else:
                    if isMagic(grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1], 
                               grid[i][j-1], grid[i][j], grid[i][j+1], 
                               grid[i+1][j-1], grid[i+1][j], grid[i+1][j+1]
                              ):
                        count+=1
        return count
