class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s:
            return False
        q = [s]
        while q:
            for cur in q:
                if cur.val == t.val and self.isSameTree(cur, t):
                    return True
            q = [child for cur in q for child in (cur.left, cur.right) if child]
        return False
    
    def isSameTree(self, a, b):
        """
        :type a: TreeNode
        :type b: TreeNode
        :rtype: bool
        """
        if not (a or b):
            return True
        if not (a and b) or a.val != b.val:
            return False
        return self.isSameTree(a.left, b.left) and self.isSameTree(a.right, b.right)
