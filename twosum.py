class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        holder = {}

        #
        #
        #
        #
        index = 0

        for i in range(len(nums)):
            ans = target - nums[i]
            if ans in holder:
                return holder[ans], i
            else:
                holder[nums[i]] = i
