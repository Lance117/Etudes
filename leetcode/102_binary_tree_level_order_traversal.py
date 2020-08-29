class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res, q = [], [root]
        if not root: return []
        while q:
            res.append([curr.val for curr in q])
            q = [child for curr in q for child in (curr.left, curr.right) if child]
        return res

    def levelOrder2(self, root):
        """
        recursive solution
        """
        def levelHelper(node, lvl):
            if not node:
                return
            if not res or len(res) < lvl:
                res.append([])
            res[lvl - 1].append(node.val)
            levelHelper(node.left, lvl + 1)
            levelHelper(node.right, lvl + 1)

        res = []
        levelHelper(root, 1)
        return res
