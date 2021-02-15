# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:        
        def trav(node):
            if not node:
                return 0
            nonlocal res
            left = max(0, trav(node.left))
            right = max(0, trav(node.right))
            res = max(res, left + right + node.val)
            return max(left, right) + node.val
        
        res = -float('inf')
        trav(root)
        return res
