class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for letter in s:
            stack.append(letter)
        alphastring = ""
        final = ""
        while stack:
            cur = stack.pop()
            print(cur)
            if cur.isalpha():
                alphastring = cur + alphastring
                print("alphastring : " + alphastring)
                continue
                
            elif cur == "[":
                cur = stack.pop()
                final = alphastring * int(cur) + final
                print("final: " + final)
                alphastring = ""

                continue

                

        return final
            