class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """ 
#       1. if the last element is not 9, just add one; if is 9, set the element to 0 all the way back to the first element that is not 9.  
        # if all the elements are 9, set all to 0 and add [1] before the array
        # if digits[-1] == 9:
        #     i = len(digits)-1
        #     while(digits[i]==9):
        #         digits[i] = 0
        #         i -= 1
        #         if i < 0:
        #             return [1]+digits
        #     digits[i] += 1
        #     return digits
        # else:
        #     digits[-1] += 1
        #     return digits
        
#       2. simple one , convert it to int, add 1. convert back to list
        digits = ''.join([str(digit) for digit in digits])
        digits = int(digits) + 1
        return [int(digit) for digit in str(digits)]
        
