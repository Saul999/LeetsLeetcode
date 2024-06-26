# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(root, max_val):
            if not root:
                return 0
            
            good_nodes = 0
            if root.val >= max_val:
                good_nodes += 1
            max_val = max(max_val, root.val)
            
            # Update the count by recursively exploring left and right subtrees
            good_nodes += dfs(root.left, max_val)
            good_nodes += dfs(root.right, max_val)
            
            return good_nodes
        
        # Start the DFS traversal from the root with the initial max value as the root's value
        return dfs(root, root.val)