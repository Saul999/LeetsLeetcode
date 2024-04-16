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
        def dfs(root, array):
            
            if not root:
                return None
            array.append(root.val)
            dfs(root.right, array)
            return array
        final = []
        
        return dfs(root, final)