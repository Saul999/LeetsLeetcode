class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        
        # 56/123 tests cases need to fix the string sizes instead of stopping the 
        # ex length AB should be ABAB if the str1 is ABABABAB and str2 is ABAB
        newstring = ""
        start = str1[0]
        for i in str1: 
            if i in newstring and i == start:
                break
            newstring += i
            
        if newstring in str2:
            return newstring
        else:
            return ""