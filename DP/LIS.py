class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LS = [1] * len(nums)
        maxSub = 1
        for i in range(len(nums) - 1, -1, -1):
            highestJ = 0
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    LS[i] = max(LS[i], LS[j] + 1)
                maxSub = max(maxSub, LS[i])
        return maxSub
            # check everything right is > than in len(n) to get max 
            # store max LIS[index] 
            # move next pos and repeat
            # return max sub in var


            