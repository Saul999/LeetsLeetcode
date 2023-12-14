class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mappedS = defaultdict(int)
        mappedT = defaultdict(int)
        n = len(s)

        if n != len(t):
            return False

        for i in range(n):
            mappedS[s[i]] += 1

        for i in range(n):
            mappedT[t[i]] += 1

        print(mappedS)
        if mappedS == mappedT:
            return True

        return False
        print(mappedS)
