class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 1:
            return nums
        #length nums = 4
        #nums = 3
        #leftptr = 1
        #rightptr = 4
        leftptr = 0
        rightptr = 1
        leftval = 0
        rightval = 0
        

        #2 ptrs move together and swapping values
        for i in range(len(nums)):
            # print('right ' + str(rightptr) +' '+ str(nums[rightptr]))
            # print("left " + str(leftptr) + " " + str(nums[leftptr]))
            if rightptr == len(nums):
                break
            if nums[leftptr] == 0 and nums[rightptr] == 0 and (rightptr + 1) < len(nums):
                leftval = nums[leftptr]
                rightval = nums[rightptr + 1]
                nums[rightptr + 1] = leftval
                nums[leftptr] = rightval   
                if nums[leftptr] == 0 and (rightptr + 2) < len(nums):
                    leftval = nums[leftptr]
                    rightval = nums[rightptr + 2]
                    nums[rightptr + 2] = leftval
                    nums[leftptr] = rightval  
            if nums[leftptr] == 0:
                leftval = nums[leftptr]
                rightval = nums[rightptr]
                nums[leftptr] = rightval
                nums[rightptr] = leftval
            
            leftptr +=1
            rightptr += 1

        # new solution throw 0 to the back
        # for i in range(len(nums)):
        #     if nums[leftptr] == 0:


        print(nums)
        return nums