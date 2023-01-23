import re


def isMatch(s: str, p: str) -> bool:

    p = ''.join(set(p))
    p = r"{}".format(p)
    p = re.compile(p)
    if p.fullmatch(s):
        return True
    else:
        return False


s = "aa"
p = "a*"

print(isMatch(s, p))
