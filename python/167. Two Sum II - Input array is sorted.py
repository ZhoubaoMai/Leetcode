class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
#       1. brute force (time limit exceeded)
        # for i in range(len(numbers)):
        #     for j in range(i+1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1, j+1]

#       2. two pointer, use two pointer to indicate the first and second element in the array
#          if the sum of the two element is bigger than target, the index of second element decrease; 
#          otherwise, the index of the first element increse
        first = 0
        second = len(numbers)-1
        while first < second:
            currentSum = numbers[first] + numbers[second]
            if currentSum == target:
                return [first+1, second+1]
            elif currentSum > target:
#               if there are many identical numbers in the array, it may cause time limit exceed
#               thus, find the nearest number that is not equal to second
                num = numbers[second]
                while(num == numbers[second]):
                    second -= 1
            else:
                num = numbers[first]
                while(num == numbers[first]):
                    first += 1


