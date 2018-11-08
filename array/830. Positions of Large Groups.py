class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        largeGroup=list()
        count, left, right =1, 0, 0
        for i in range(1, len(S)):
            if S[i] == S[i-1]:
                count += 1
                right += 1
            else:
                if count>=3:
                    largeGroup.append([left,right])                    
                count = 1
                left = i
                right = i
        if count >=3:
            largeGroup.append([left,right])
        return largeGroup
                
            
            
