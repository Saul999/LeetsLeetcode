class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ltotal = 0
        preSum = 0
        total = sum(nums)

        for i in range(len(nums)):
            print("left " + str(ltotal))
            righttotal = total - nums[i] - ltotal
            print("index " + str(i))
            if ltotal == righttotal:
                return i
            ltotal += nums[i]
            print("right " + str(righttotal))
        return -1

        print(righttotal)            
            
        # while postSum != preSum:
        #     print(nums[lptr])
        #     preSum += nums[lptr]
        #     print("presum " + str(preSum))
        #     postSum += nums[rptr]
        #     print(nums[rptr])
        #     print("postsum " + str(postSum))

        #     rptr -= 1
        #     lptr += 1
        # return rptr