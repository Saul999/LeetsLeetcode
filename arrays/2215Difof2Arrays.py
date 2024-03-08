class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        first = set()
        second = set()
        
        for i in nums1:
            if i not in nums2:
                first.add(i)
        for i in nums2:
            if i not in nums1:
                second.add(i)
                
        return[first, second]