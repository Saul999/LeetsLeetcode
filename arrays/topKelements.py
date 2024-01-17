class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []
        finalAns = {}
        adder = 1

        if len(nums) <= 1:
            return nums
        if len(nums) == 2 and nums[0] == nums[1]:
            return [nums[0]]

        for i in range(len(nums) - 1):
            print("NEW")
            print("adder: " + str(adder))
            print("nums[i]: " + str(nums[i]))
            print("nums[i + 1] " + str(nums[i + 1]))
            if nums[i] == nums[i + 1]:
                adder += 1

            else:
                finalAns[nums[i]] = adder
                print("else adder: " + str(adder))
                adder = 1

        for i in range(len(finalAns) - 1):
            if finalAns[i] > k:
                break
        return finalAns
