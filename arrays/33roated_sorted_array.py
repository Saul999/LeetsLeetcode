class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        end_val = nums[-1]
        n = len(nums) - 1
        pivot = n - end_val
        left = 0
        right = 0
        print(left)
        
        if target > pivot and target > end_val:
            right = pivot

        elif target > pivot and target < end_val:
            left = pivot
            right = n

        mid = left + right // 2
        print(mid)
        while left < right:
            if target > nums[left]:

