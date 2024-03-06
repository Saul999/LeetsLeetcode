class Solution(object):
    def decodeString(self, s):
        stack = []
        current_num = 0
        current_str = ""

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char.isalpha():
                current_str += char
            elif char == "[":
                stack.append((current_str, current_num))
                print("stack: " + str(stack))
                current_str = ""
                current_num = 0
            elif char == "]":
                prev_str, prev_num = stack.pop()
                print("prevstr: " + prev_str)
                print("prevnum: " + str(prev_num))
                current_str = prev_str + current_str * prev_num
                print("cur string: " + current_str)

        return current_str
