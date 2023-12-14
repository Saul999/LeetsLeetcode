from collections import defaultdict


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # brute force time limite exceeded 65/75 testcases passed
        """
        lenghtofnums = len(nums)
        for i in range(lenghtofnums):
            for j in range(i + 1, lenghtofnums):
                if nums[i] == nums[j]:
                    return True
        return False
        """
        n = len(nums)
        counter = 0

        mapped = defaultdict(int)
        for i in range(n):
            if nums[i] in mapped:
                return True
            mapped[nums[i]]
        return False
