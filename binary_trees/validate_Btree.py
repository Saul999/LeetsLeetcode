# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # left side  < root
        def dfs(root, left, right):
            if not root:
                return False
            if root.left < root and root.right > root:
                return True
            else: 
                return False
            if root.left:
                dfs(root.left,"-inf", root)
            if root.right:
                dfs(root.right, right, "inf")
            
        return dfs(root, "-inf", "inf")