"""
Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.

1. Find what choices we have - nums list
2. For each choice:
    a. Make choice, and explore recursively by passing info for next choice
    b. Undo choice and explore other paths without that choice
3. Base case: when nothing else to choose, add auxiliary list to the results
"""

def subsets(nums):
    res = []

    def list_subsets_rec(idx=0, aux=[]):
        if idx == len(nums):
            res.append(aux[:])    
            return
        aux.append(nums[idx])
        list_subsets_rec(idx+1, aux)
        aux.pop()
        list_subsets_rec(idx+1, aux)
    
    list_subsets_rec()
    return res