class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
#       if the character start with '0' then it must be a one-bit charcter, jump the index to the next one (index = index + 1)
#       if the character starts with '1' then it must be a two-bits character, jum to the next character (index = index + 2)
#       if follow the step above can jump to the end of the string, then the string can convert to serveral bits
        bits = bits[:-1]
        i = 0
        while True:
            if i == len(bits):
                return True
            elif i == len(bits) + 1:
                return False
            if bits[i] == 0:
                i += 1
            else:
                i += 2
