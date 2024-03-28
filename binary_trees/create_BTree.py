class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = Node(20)
b = Node(5)
c = Node(3)
d = Node(9)
e = Node(10)
f = Node(6)

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
    res = 0
    while stack:
        cur = stack.pop()
        res += cur.val
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
    print(res)
    return res

def dfs_recursion(root):
    if root:
        if root.val == 'e':
            return True
        dfs(root.left)
        dfs(root.right)
    return False


# gets min and returns it
def bfs(root):
    if root == None:
        return []
    queue = [root]
    min = 10000
    while queue:
        cur = queue.pop(0)
        if cur.val < min:
            copy = cur
            min = cur.val
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)
    print(min)
    return False
    

# dfs_recursion(a)
bfs(a)
# dfs_recursion(a)
dfs(a)


