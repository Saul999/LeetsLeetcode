class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        newlist = list(s)
        # vowels = {"a": 0, "e": 0, "i": 0 , "o": 0 ,"u": 0}
        vowels = "aeiou"
        lptr = 0
        vowelsCnt = 0
        maxVowels = 0
        for i in range(k):
            if s[i] in vowels:
                vowelsCnt += 1
        maxVowels = vowelsCnt
        for i in range(k, len(s)):
            if s[lptr] in vowels:
                vowelsCnt -= 1
            if s[i] in vowels:
                vowelsCnt += 1
            if maxVowels < vowelsCnt:
                maxVowels = vowelsCnt
            lptr+= 1
        return maxVowels
