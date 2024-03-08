class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        mapped = {}
        final = [[],[]]
        first = set()
        second = set()
        
        for i in nums1:
            if i in nums2:
                mapped[i] = i
        
        for i in range(len(nums1)):
            print(i)
            print("nums1 " + str(nums1[i]))
            if nums1[i] in mapped:
                continue
            else:
                first.add(nums1[i])

        for i in range(len(nums2)):
            print(i)
            print("nums2 " + str(nums2[i]))
            if nums2[i] in mapped:
                continue
            else:
                second.add(nums2[i])

        final = [first, second]
        print(mapped)
        return final
                
        
                
