# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # def dfs(root, array):
            
        #     if not root:
        #         return None
        #     array.append(root.val)
        #     dfs(root.right, array)
        #     return array
        # final = []
        
        # return dfs(root, final)
        queue = [root]
        rightMost = []
        def bfs(root):
            while queue:

                rightside = None
                lenQ = len(queue)
                for i in range(lenQ):
                    node = queue.pop(0)
                    if node:
                        rightside = node
                        queue.append(node.left)
                        queue.append(node.right)
                if rightside:
                    rightMost.append(rightside.val)
                

        bfs(root)
        return rightMost

                    
