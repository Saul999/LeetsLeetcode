class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftptr = 0
        rightptr = len(height) - 1
        maxArea = 0
        minPtr = 0
        distance = 0
        # if len(height) < 1:
        #     return 1
        while leftptr < rightptr:
            minPtr = min(height[rightptr], height[leftptr])
            distance = rightptr - leftptr
            if maxArea < (distance *  minPtr):
                maxArea = distance * minPtr
            if minPtr == height[rightptr]:
                rightptr -= 1
            if minPtr == height[leftptr]:
                leftptr += 1
            
        return maxArea
        
        