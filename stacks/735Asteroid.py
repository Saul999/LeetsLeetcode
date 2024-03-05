class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = [0] * len(asteroids)
        absVal1 = 0
        absVal2 = 0
        print(asteroids[-2])
        for i in range(len(asteroids)):
            if len(asteroids) < 2:
                return asteroids
            if asteroids[-1] < 0:
                if asteroids[-2] > 0:
                    if abs(asteroids[-1]) > abs(asteroids[-2]):
                        stack.append(asteroids.pop())
                    else:
                        asteroids.pop()
                        stack.append(asteroids.pop())

            elif asteroids[-1] > 0 and asteroids[-2] > 0:
                stack.append(asteroids.pop())
                stack.append(asteroids.pop())
            
                    
        return stack