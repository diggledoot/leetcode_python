def test(digits):
    key_char_map = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    if digits == "":
        return []

    letter_combinations = [key_char_map[digit] for digit in digits]  # [[a,b,c],[d,e,f]]

    permutations = [""]
    for letters in letter_combinations:
        new_permutations = []
        for letter in letters:
            for perm in permutations:
                new_permutations.append(perm + letter)
        permutations = new_permutations

    result = []
    for perm in permutations:
        result.append(perm)

    return result


print(test("23"))
