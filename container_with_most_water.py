from typing import List

"""
O(n^2) - pretty bad
"""


def bruteForceMaxArea(height: List[int]) -> int:
    res = 0
    for left in range(len(height)):
        for right in range(left+1, len(height)):
            area = (right - left) * min(height[left], height[right])
            res = max(res, area)
    return res

# O(n)


def maxArea(height: List[int]) -> int:
    # Initialize result variable
    result = 0

    # Initialize left and right pointers
    left, right = 0, len(height) - 1

    # It's pointless if left == right index
    while left < right:

        """
        Regular area calculation, length * height, 
        but we want the minimum height between the pointers
        otherwise the water would just overflow
        """
        area = (right-left) * min(height[left], height[right])

        # Update result
        result = max(result, area)

        # Since the limiting factor is the shortest height, move the pointer either left or right.
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return result


heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(heights))
