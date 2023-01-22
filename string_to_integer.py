import re
def myAtoi(s: str) -> int:
    MAX, MIN = 2147483647, -2147483648
    s = re.findall(r'[-+]?\d+', s) #extract number from string with sign
    try:
        res = int(''.join(s))
    except:
        return 0
    if res > MAX:
        return MAX
    if res < MIN:
        return MIN
    return res


print(myAtoi("words and -4193"))
