class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 1. two pointer
        # start = 0
        # end = len(height)-1
        # h = 0
        # maxVolumn = 0
        # while start < end:
        #     smaller = height[start] if height[start] < height[end] else height[end]
        #     while h  < smaller:   #  可以直接求出来我当时为什么要写循环... 对自己无语
        #         h  += 1
        #     temp = h  * (end-start)
        #     maxVolumn = max(temp, maxVolumn)
        #     if smaller == height[start]:
        #         start += 1
        #     if smaller == height[end]:
        #         end -= 1
        # return maxVolumn
        
        start = 0
        end = len(height)-1
        maxVolumn = 0
        while start < end:
            smaller = height[start] if height[start] < height[end] else height[end]
            temp = smaller  * (end-start)
            maxVolumn = max(temp, maxVolumn)
            if smaller == height[start]:
                start += 1
            if smaller == height[end]:
                end -= 1
        return maxVolumn
