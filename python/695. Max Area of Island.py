import math
class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 1. DFS recursive version        
#         def adj(node, grid):
#             adjNode = []
#             for v in[(node[0]-1, node[1]), (node[0]+1, node[1]), (node[0], node[1]-1), (node[0], node[1]+1)]:
#                 i, j = v[0], v[1]
#                 if 0<=i<=len(grid[0])-1 and 0<=j<=len(grid)-1 and grid[j][i] == 1:
#                     adjNode.append(v)
#             return adjNode
        
#         def DFS(u, area, visited, grid):
#             area += 1
#             visited.add(u)
#             for v in adj(u, grid):
#                 if v not in visited:
#                     area = DFS(v, area, visited, grid)
#             return area
        
        
#         visited = set()
#         maxArea = 0
#         for j in range(len(grid)):
#             for i in range(len(grid[0])):
#                 if grid[j][i] == 1 and (i,j) not in visited:
#                     area = 0
#                     area = DFS((i,j), area, visited, grid)
#                     if area > maxArea:
#                         maxArea = area        
#         return maxArea
    
        # 2. simple version of DFS
        visited = set()
        
        def area(i , j):
            if 0<=j<=len(grid)-1 and 0<=i<=len(grid[0])-1 and (i,j) not in visited and grid[j][i] == 1:
                visited.add((i,j))
                return 1 + area(i, j-1) + area(i, j+1) + area(i-1, j) + area(i+1, j)
            else:
                return 0
        
        maxArea = 0
        for j in range(len(grid)):
            for i in range(len(grid[0])):
                temp = area(i,j)
                if temp > maxArea:
                    maxArea = temp
        return maxArea

        
        # 3.improvement of 2, not using a set to record visited, set the value = 0 if visited the node
        # and do the conditional judgement seperately         
        def area(i , j):
            if 0<=j<=len(grid)-1 and 0<=i<=len(grid[0])-1 and grid[j][i]:
                grid[j][i] = 0
                return 1 + area(i, j-1) + area(i, j+1) + area(i-1, j) + area(i+1, j)
            else:
                return 0
        maxArea = 0
        for j in range(len(grid)):
            for i in range(len(grid[0])):
                temp = area(i,j)
                if temp > maxArea:
                    maxArea = temp
        return maxArea

