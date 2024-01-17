class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []
        adder = 1

        if len(nums) <= 1:
            return nums
        for i in range(len(nums) - 1):
            print("NEW")
            print("adder: " + str(adder))
            print("nums[i]: " + str(nums[i]))
            print("nums[i + 1] " + str(nums[i + 1]))
            if nums[i] == nums[i + 1]:
                adder += 1

            else:
                ans.append(nums[i])
                print("else adder: " + str(adder))
                adder = 0
        return ans
