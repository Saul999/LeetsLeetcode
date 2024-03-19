class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        # if s[0] != "[" or "(" or "{":
        #     return False

        # mapped = {'(' :0, '{' : 0, '[': 0}
        # backends = {')' :0, '}' : 0, ']': 0}
        mapped = {')' :'(', '}' : '{', ']': ']'}

        # for i in range(len(s)):
        #     if s[i] in mapped:
        #         mapped[s[i]] += 1
        #     elif s[i] in backends:
                
        for i in range(len(s)):
            if s[i] in mapped:
                if stack and (stack[-1] == mapped[s[i]]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        if not stack:
            return True
        else:
            False
                

        
        