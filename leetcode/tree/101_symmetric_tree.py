# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        def symHelper(l, r):
            if not (l or r):
                return True
            if not (l and r) or l.val != r.val:
                return False
            out_branch = symHelper(l.left, r.right)
            in_branch = symHelper(l.right, r.left)
            return out_branch and in_branch
        
        return symHelper(root.left, root.right)

        def isSymmetricIter(self, root: TreeNode) -> bool:
            if not root:
                return True
            s = [root.left, root.right]
            while s:
                r = s.pop()
                l = s.pop()
                if not (l or r):
                    continue
                if not (l and r) or l.val != r.val:
                    return False
                s.append(l.left)
                s.append(r.right)
                s.append(l.right)
                s.append(r.left)
            return True
