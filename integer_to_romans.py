def intToRoman(number: int) -> str:
    symbol_list = [
        ["I", 1],
        ["IV", 4],
        ["V", 5],
        ["IX", 9],
        ["X", 10],
        ["XL", 40],
        ["L", 50],
        ["XC", 90],
        ["C", 100],
        ["CD", 400],
        ["D", 500],
        ["CM", 900],
        ["M", 1000]
    ]
    result = ""
    for symbol, value in reversed(symbol_list):
        if number // value:  # Check if can be integer divided is 0
            count = number//value
            result += (symbol*count)
            number = number % value
    return result


print(intToRoman(1994))
