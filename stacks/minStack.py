class MinStack(object):

    def __init__(self):
        self.items = []
        self.min = 9999999999
        self.minstack = []

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        return False

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.items.append(val)
        # if self.minstack:
        #     self.min = val
        # else self.minstack[-1] > val:
        #     pass
        # self.minstack.append(self.min)
        val = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        self.minstack.pop()
        return self.items.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.items[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()