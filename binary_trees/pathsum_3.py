# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        def dfs(root, targetSum, val, outputVal):
            if not root:
                return None
            
            val += root.val
            if val == targetSum:
                outputVal += 1
                dfs(root.left, targetSum, 0, outputVal)
                dfs(root.right, targetSum, 0, outputVal)
                

            else:
                dfs(root.left, targetSum, val, outputVal)
                dfs(root.right, targetSum, val, outputVal)
                
            return outputVal
        return dfs(root, targetSum, 0, 0)