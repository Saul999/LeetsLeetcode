# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        def dfs(root, value):
            if not root:
                return None

            value += root.val
            
            if value == targetSum:
                return True
            
            if not root.left and not root.right:
                value -= root.val
            dfs(root.left, value)
            dfs(root.right, value)

            return False
            
        
        return dfs(root, 0)
