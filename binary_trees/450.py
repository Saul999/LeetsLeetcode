# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None

        if root.val == key:
            # 1 right child
            if not root.left and root.right: return root.right
            # 1 left child
            if not root.right and root.left: return root.left
            # no children
            if not root.left and not root.right:
                return None
            # 2 children
            pnt = root.right
            while pnt.left: pnt = pnt.left
            root.val = pnt.val
            root.right = self.deleteNode(root.right, root.val)
        else:
            if root.val < key:
                root.right = self.deleteNode(root.right, key)
            else:
                root.left = self.deleteNode(root.left, key)
        return root