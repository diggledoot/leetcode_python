def test(nums, target):
    nums.sort()
    closest = float("inf")

    for i in range(len(nums) - 2):  # needed to form triplets, have at least 2
        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if abs(target - total) < abs(target - closest):
                closest = total

            if total < target:  # if total is too small, move left
                left += 1
            elif total > target:  # if total is too large, move right
                right -= 1
            else:
                return total  # if total is equal to target

    return closest


print(test([-1, 2, 1, -4], 1))
