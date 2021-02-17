# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inorder_to_idx = {x: i for i, x in enumerate(inorder)}
        pre_iter = iter(preorder)
        def helper(left, right):
            if right < left:
                return None
            root_val = next(pre_iter)
            root_node = TreeNode(root_val)
            root_idx = inorder_to_idx[root_val]
            root_node.left = helper(left, root_idx - 1)
            root_node.right = helper(root_idx + 1, right)
            return root_node
        return helper(0, len(inorder) - 1)
