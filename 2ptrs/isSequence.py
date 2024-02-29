class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # svals = {}
        # count = 0
        # order = 0
        # for i in range(len(s)):
        #     svals[s[i]] = i
        # print(svals)
        # for j in t:
        #     if j in svals:
        #         count+= 1
        # if count == len(s):
        #     return True
        # return False
        if len(s) < 1:
            return True
        sptr = 0
        tptr = 0
        count = 0
        for i in range(len(t)):
            if s[sptr] == t[tptr]:
                sptr += 1
                count += 1
                print(count)
            if count == len(s):
                return True
            tptr += 1
        
        print(count)
        return False        

