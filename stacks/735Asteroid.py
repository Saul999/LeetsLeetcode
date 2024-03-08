#REATTEMPT FROM  3/7/24 PASSED MOST OPTIMAL SOLUTION


class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for i in range(len(asteroids)):
            if asteroids[i] > 0:
                stack.append(asteroids[i])
            if asteroids[i] < 0:
                while stack and stack[-1] > 0:
                    if (abs(asteroids[i]) > abs(stack[-1])):
                        stack.pop()
                    elif abs(asteroids[i]) == abs(stack[-1]):
                        stack.pop()
                        break
                    else: 
                        break
                    
                else:
                    stack.append(asteroids[i])
                    
            

        return stack


# class Solution(object):
#     def asteroidCollision(self, asteroids):
#         """
#         :type asteroids: List[int]
#         :rtype: List[int]
#         """
#         stack = []

#         for a in asteroids:
#             if a > 0:
#                 stack.append(a)
#             else:
#                 while stack and stack[-1] > 0:
#                     if stack[-1] == abs(a):
#                         stack.pop()
#                         break
#                     elif stack[-1] < abs(a):
#                         stack.pop()
#                     else:
#                         break
#                 else:
#                     stack.append(a)

        # return stack

    