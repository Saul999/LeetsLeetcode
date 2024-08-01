class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        numbers_set = set(nums)
        max_seq = 0
        
        for num in numbers_set:  
            if num - 1 not in numbers_set: 
                current_num = num
                current_streak = 1

                while current_num + 1 in numbers_set:
                    current_num += 1
                    current_streak += 1

                max_seq = max(max_seq, current_streak)
        
        return max_seq