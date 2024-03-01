class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = list(s)
        newStack = []
        count = 0

        for i in range(len(stack) - 1, -1, -1):
            if stack[i] == "*":
                count += 1
            elif count > 0:
                count-= 1
            else:
                newStack.append(stack[i])



        #attempt 2
        # count = 0
        # for i in range(len(s)):
        #     if s[i] == "*":
        #         i += 2
        #     else:
        #         newStack.append(s[i])

        newStack.reverse()
        return "".join(newStack)