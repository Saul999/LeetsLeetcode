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
        contString = ""
        
        count = 0
        while stack:
            cur = stack[-1]
            if cur.isalpha():
                alphastring = cur + alphastring
                print("alphastring : " + alphastring)   
             
            elif cur == "[":
                cur = stack.pop()
                count -= 1      
                if count > 0:    
                    cur = stack.pop()
                    contString = alphastring + contString
                    print(contString)
                    alphastring = ""
                if count == 0:
                    cur = stack.pop()
                    final = (alphastring * int(cur)) + contString
            elif cur == "]":
                count+= 1
                cur= stack.pop()
            if stack:
                cur = stack.pop()
            else: 
                break




                

        return final
            