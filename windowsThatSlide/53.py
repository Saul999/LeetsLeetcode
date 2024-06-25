class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = nums[0]
        value = 0
        for i in nums:
            if value < 0:
                value = 0
            value += i
            max_val = max(max_val, value)
        return max_val
