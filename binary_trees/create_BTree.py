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

#Tree Example
    #     a
    #    / \
    #   b   c 
    #  / \    \
    # d   e    f  



def dfs(root):
    if root == None:
        return []
    stack = [root]
    res = []
    while stack:
        cur = stack.pop()
        res.append(cur)
        print(cur.val)
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
        

def dfs_recursion(root):
    if root:
        dfs(root.left)
        print(root.val)
        dfs(root.right)
    
        

dfs_recursion(a)



