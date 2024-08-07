# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #checks if null
        if not root:
            return None

        #levels return
        levels = []

        def bfs(root, levels):
            #initial queue
            q = deque([root])
            while q:
                newlevel = []
                sizeofLevel = len(q)
                for i in range(sizeofLevel):
                    node = q.popleft()
                    newlevel.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                levels.append(newlevel)
                

        bfs(root,levels)

        return levels

                    
