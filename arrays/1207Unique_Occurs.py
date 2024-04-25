class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        occurs = {}
        for letter in arr:
            if letter in occurs:
                occurs[letter] += 1
            else:
                occurs[letter] = 1
        
        print(occurs.values())

        occursSet = set()
        for key in occurs:
            if occurs[key] in occursSet:
                return False
            occursSet.add(occurs[key])

        return True
        print(occursSet)