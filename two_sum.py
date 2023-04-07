from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    values = {}  # initialize key value pair

    for index, value in enumerate(nums):
        if target - value in values:
            return [values[target - value], index]  # return indices in a list

        else:
            values[value] = index


"""
Long explanation:

Initialize an empty values dictionary. For reference, a dictionary is a key-value data structure.

Iterate over the passed in list. Enumerate to grab the index.

Check if the difference between the target and current value is in values. It is looking for the key.

If not, add the current value as key and its index into the values dictionary.

"""
