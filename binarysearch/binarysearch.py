class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #        l m r  9
        #  0 1 2 3 4 5
        # [-1 0 3 5 9 12]

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) / 2
            if nums[mid] < target:
                print("first")
                print("left " + str(l))
                print("mid " + str(mid))
                print("right " + str(r))
                l = mid
            elif nums[mid] > target:
                print("second")
                print("left " + str(l))
                print("mid " + str(mid))
                print("right " + str(r))
                r = mid
            elif nums[mid] == target:
                print("mid 2: " + str(mid))
                return mid
            else:
                return -1

        return -1
