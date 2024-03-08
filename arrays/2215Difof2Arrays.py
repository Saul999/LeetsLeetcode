class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        mapped = {}
        final = [[],[]]
        first = []
        second = [] 
        
        for i in nums1:
            if i in nums2:
                mapped[i] = i
        
        for i in range(len(nums1)):
            print(i)
            print("nums1 " + str(nums1[i]))
            if nums1[i] in mapped and nums2[i] in mapped:
                print("both worked")
                continue
            elif nums1[i] in mapped and nums2[i] not in second:
                print("nums1 worked")
                second.append(nums2[i])
            elif nums2[i] in mapped and nums1[i] not in first:
                print("nums2 worked")
                first.append(nums1[i])
            else:
                first.append(nums1[i])
                second.append(nums2[i])

            

        final = [first, second]
        print(mapped)
        return final
                
        
                
