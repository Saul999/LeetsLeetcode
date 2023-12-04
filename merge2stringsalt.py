class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        lengthofW = len(word1) + len(word2)
        final = []
        i = 0
        while i < len(word1) and i < len(word2):
            final.append(word1[i])
            final.append(word2[i])
            i += 1
        final.append(word1[i:])
        final.append(word2[i:])

        return "".join(final)

        # for i in word1:
        #   final+= word1[i]
        #   final+= word2[i]

        return final
