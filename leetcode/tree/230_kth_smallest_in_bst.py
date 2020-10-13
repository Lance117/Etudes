# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        values = []
        self.inorder(root, values)
        return values[k - 1]
        
    def inorder(self, root, values):
        if not root:
            return
        self.inorder(root.left, values)
        values.append(root.val)
        self.inorder(root.right, values)
