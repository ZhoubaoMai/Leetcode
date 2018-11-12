class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        # 1. suppose there is no overlap, the poison time is duration * attack time.
        # Then minus the overlap poison time
        
        # poisonTime = duration * len(timeSeries)
        # for i in range(len(timeSeries)-1):
        #     poisonTime -= duration - (timeSeries[i+1] - timeSeries[i]) if timeSeries[i+1] - timeSeries[i] < duration else 0
        # return poisonTime
        
        # 2. jump the position to the time + duration is overlap exisit
        if not timeSeries: return 0
        pretime = timeSeries[0]
        poison = 0
        for time in timeSeries:
            if time < pretime + duration:
                poison += time - pretime
            else:
                poison += duration
            pretime = time              
        poison += duration 
        return poison
        

