def fizzbuzz(max: int) -> None:
    res = []

    for i in range(1, max + 1):
        if i % 3 == 0 and i % 5 == 0:
            res.append(f"FizzBuzz ({i})")
            continue
        elif i % 3 == 0:
            res.append(f"Fizz ({i})")
            continue
        elif i % 5 == 0:
            res.append(f"Buzz ({i})")
            continue
        else:
            # res.append(str(i))
            continue
    return res


print(fizzbuzz(15))
