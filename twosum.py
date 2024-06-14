# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         # holder = {}

        # #
        # #
        # #
        # #
        # index = 0

        # for i in range(len(nums)):
        #     ans = target - nums[i]
        #     if ans in holder:
        #         return holder[ans], i
        #     else:
        #         holder[nums[i]] = i

        #FINAL ATTEMPT NO HELP
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        values = {}

        for i in range(len(nums)):
            value = target - nums[i]
            if value in values:
                return [values[value],i]
            else:
                values[nums[i]] = i

