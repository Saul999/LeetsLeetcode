class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        s = s.strip()  # Remove leading and trailing whitespaces
        length = len(s)
        output = ""
        word = ""

        for i in range(length):
            if s[i] == " ":
                # If the current character is a space, check if the previous character was also a space
                if i > 0 and s[i - 1] == " ":
                    continue  # Skip adding the space if it's consecutive
                output = " " + word + output
                word = ""
            else:
                word += s[i]

        output = word + output
        return output
