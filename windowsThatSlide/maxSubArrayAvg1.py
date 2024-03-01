class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        windowSum = 0
        maxAvg = 0
        lptr = 0
        rptr = k

        for i in range(k):
            windowSum+= nums[i]
        maxAvg = float(windowSum) / float(k)

        for i in range(k, len(nums)):
            windowSum -= nums[lptr]
            windowSum += nums[i]
            maxAvg = max(maxAvg, float(windowSum)/ float(k))
            lptr += 1
            
            

        return maxAvg