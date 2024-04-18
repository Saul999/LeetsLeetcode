# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        def bfs(root):
            currentlvl = 1
            max_level_sum = root.val
            max_level = 1
            while queue:
                lenQ = len(queue)
                level_sum = 0
                for i in range(lenQ):
                    node = queue.pop(0)
                    if node:
                        level_sum += node.val
                        if node.left:
                            queue.append(node.left)
                        if node.right:
                            queue.append(node.right)
                if level_sum > max_level_sum:
                    max_level_sum = level_sum
                    max_level = currentlvl
                            
                currentlvl += 1

            return max_level

        
        
        return bfs(root)
            
