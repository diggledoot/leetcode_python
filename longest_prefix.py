from typing import List


def longestCommonPrefix(strings: List[str]) -> str:
    res = ""

    for i in range(len(strings[0])):
        for s in strings:
            """
            If i equals to length of s then it is considered out of bounds
            Or if character at index i for s is not equal to the character at the first string at index i
            Then return the string of the longest common prefix
            """
            if i == len(s) or s[i] != strings[0][i]:
                return res
        res += strings[0][i]

    return res
