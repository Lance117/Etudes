"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Backtracking: choose and explore, unchoose, and base case to add auxiliary list if the list
contains k numbers.

Time complexity: T(n) = C(n,k) = kn + T(n-1) + T(n-2) + ...+ T(2) + T(1) = O(2^n)
Space complexity: O(k)
"""

def combine(n, k):
    res = []

    def combine_list(start=1, aux=[]):
        if len(aux) == k:
            res.append(aux[:])
            return
        for num in range(start, n + 1):
            aux.append(num)
            combine_list(num+1, aux)
            aux.pop()

    combine_list()
    return res