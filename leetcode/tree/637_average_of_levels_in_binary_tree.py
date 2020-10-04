"""
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def average_of_levels(root):
    """
    Simple idea to do level order traversal and record the average.
    
    Time complexity: O(n). Reads each element for lvl list and sum.
    Space complexity: O(n) - num of elements in each level depends on how deep
    the tree runs and the branching factor
    """
    lvl, res = [root], []
    while lvl:
        res.append(sum([node.val for node in lvl]) / len(lvl))
        lvl = [child for node in lvl for child in (node.left, node.right) if child]
    return res
