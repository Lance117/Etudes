"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

- The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold 
additional elements from nums2.
"""

def merge(nums1, m, nums2, n):
    """Start at end, keep track of index to write, and write the larger value of the two arrays"""
    a, b, write_idx = m - 1, n - 1, m + n - 1
    while a >= 0 and b >= 0:
        if nums1[a] > nums2[b]:
            nums1[write_idx], a = nums1[a], a - 1
        else:
            nums1[write_idx], b = nums2[b], b - 1
        write_idx -= 1
    while b >= 0:
        nums1[write_idx] = nums2[b]
        write_idx, b = write_idx - 1, b - 1