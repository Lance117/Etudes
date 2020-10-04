class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        """
        if tree is empty, return false
        return sum by the root value before going down a level
        if at leaf node, return true if leftover sum equals node's value
        """
        if not root:
            return False
        if not (root.left or root.right):
            return root.val == sum
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
