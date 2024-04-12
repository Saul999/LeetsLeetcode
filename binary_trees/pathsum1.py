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
                return False

            value += root.val
            
            if not root.left and not root.right:
                return value == targetSum
            
            left = dfs(root.left, value)
            right = dfs(root.right, value)

            return left or right
            
        
        return dfs(root, 0)

      