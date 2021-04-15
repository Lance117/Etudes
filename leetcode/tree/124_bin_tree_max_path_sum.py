# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = float('-inf')
        
    def maxPathSum(self, root: TreeNode) -> int:
        self.helper(root)
        return self.res
        
    def helper(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = max(0, self.helper(root.left))
        right = max(0, self.helper(root.right))
        cur = max(left, right) + root.val
        self.res = max(self.res, cur, left + right + root.val)
        return cur
