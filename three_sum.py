from typing import List

# return subarrays that equals to 0 and that each i!=j, i!=k, j!=k
def threeSum(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()

    for index, value in enumerate(nums):
        if index > 0 and value == nums[index - 1]:
            continue
        left, right = index + 1, len(nums) - 1
        while left < right:
            threeSum = value + nums[left] + nums[right]
            if threeSum > 0:
                right -= 1
            elif threeSum < 0:
                left += 1
            else:
                res.append([value, nums[left], nums[right]])
                # edge case where can be have repeated values on left and right [-2,-2, 0, 0, 2, 2]
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
    return res


print(threeSum([-1, 0, 1, 2, -1, -4]))
