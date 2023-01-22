from statistics import median
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array = nums1 + nums2
        merged_array.sort()
        return median(merged_array)

"""
Man, whatever, it works.
"""

