# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):
class Solution(object):
    def guessNumber(self, n):
        left = 1  # Change left to 1 as the numbers start from 1
        right = n
        
        while True:
            middle = (left + right) // 2  # Calculate middle using integer division
            
            result = guess(middle)
            
            if result > 0:
                left = middle + 1
            elif result < 0:
                right = middle - 1
            else:
                return middle
