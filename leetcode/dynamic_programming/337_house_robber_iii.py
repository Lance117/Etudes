# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def robber(house):
            # state: max when not robbed, max when robbed
            if not house:
                return [0, 0]
            left, right = robber(house.left), robber(house.right)
            # state: amount, cur house. choices: rob, not rob
            rob = house.val + left[0] + right[0] # can't rob directly-linked houses
            not_rob = max(left[0], left[1]) + max(right[0], right[1])
            return [not_rob, rob]
        
        res = robber(root)
        return max(res[0], res[1])
