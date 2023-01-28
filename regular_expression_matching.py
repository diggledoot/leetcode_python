import re


def isMatch(inputString: str, pattern: str) -> bool:

    pattern = "".join(set(pattern))
    pattern = r"{}".format(pattern)
    pattern = re.compile(pattern)
    if pattern.fullmatch(inputString):
        return True
    else:
        return False


s = "aa"
p = "a*"

print(isMatch(s, p))
