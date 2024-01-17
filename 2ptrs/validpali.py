class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = s.replace(" ", "")
        s = s.replace(",", "")
        s = s.replace(":", "")
        s = s.replace(".", "")
        s = s.replace("@", "")
        s = s.replace("#", "")
        s = s.replace("_", "")
        s = s.replace("[", "")
        s = s.replace("]", "")
        s = s.replace('"', "")
        s = s.replace("{", "")
        s = s.replace("}", "")
        s = s.replace("'", "")
        s = s.replace("-", "")
        s = s.replace("?", "")
        s = s.replace(";", "")
        s = s.replace("!", "")
        s = s.replace("$", "")
        s = s.replace("(", "")
        s = s.replace(")", "")
        s = s.replace("`", "")

        print(s)
        if len(s) == 0 or len(s) == 1:
            return True
        elif len(s) == 2:
            if s[0] == s[1]:
                return True
        leftptr = 0
        print(leftptr)
        rightptr = len(s) - 1
        print(rightptr)
        for i in range(len(s) - 1):
            if leftptr >= rightptr:
                return True
            if s[leftptr] == s[rightptr]:
                print(s[rightptr])
                print(s[leftptr])
                rightptr -= 1
                leftptr += 1
            else:
                return (False)
