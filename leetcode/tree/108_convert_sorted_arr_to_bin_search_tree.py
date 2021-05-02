# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        l, r = 0, len(nums) - 1
        
        def treeBuilder(start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            node = TreeNode(nums[mid])
            node.left = treeBuilder(start, mid-1)
            node.right = treeBuilder(mid+1, end)
            return node
        
        return treeBuilder(l, r)
