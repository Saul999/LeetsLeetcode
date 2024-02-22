class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        w1 = len(word1)
        w2 = len(word2)

        lengthofW = len(word1) + len(word2)
        finalword = ""
        i = 0
        while i <= lengthofW:
            if i < w1:
                finalword = finalword + word1[i]
            if i < w2:
                finalword += word2[i]
            i+=1

        return finalword