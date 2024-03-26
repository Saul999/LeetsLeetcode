class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.right = c
a.left = b
b.left = d
b.right = e
c.right = f


def dfs(root):
    stack = [root]
    while stack:
        cur = stack.pop()
        print(cur.val)
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
        

dfs(a)



