def romansToInt(s: str) -> int:
    # largest to smallest: add them up
    # smaller before larger: subtract smaller
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    res = 0
    for i in range(len(s)):
        """
        Check if index out of bounds 
        and current key value is less than next key value 
        because smaller before larger 
        """
        if i+1 < len(s) and roman[s[i]] < roman[s[i+1]]:
            res -= roman[s[i]]
        else:
            res += roman[s[i]]
    return res


print(romansToInt("MCMXCIV"))
