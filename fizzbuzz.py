

def fizzbuzz(max: int) -> None:

    res = []
    for i in range(1,max+1):
        if i % 3 == 0 and i % 5 == 0:
            res.append("FizzBuzz")
            continue
        elif i % 3 == 0:
            res.append("Fizz")
            continue
        elif i % 5 == 0:
            res.append("Buzz")
            continue
        else:
            res.append(str(i))
            continue
    return res


print(fizzbuzz(3))
