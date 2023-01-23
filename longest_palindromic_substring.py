def find_longest_palindrome(string):
    longest = ''
    length_of_string = len(string)

    if length_of_string == 1:
        return string

    if length_of_string == 2:
        if string == string[::-1]:
            return string

    for i in range(length_of_string):
        # n+1 here because we want to till the end at 13
        for j in range(i+1, length_of_string+1):
            word = string[i:j]
            if word == word[::-1]:
                if len(word) > len(longest):
                    longest = word
    return longest


print(find_longest_palindrome('locoannamadam'))
# madam

print(find_longest_palindrome("bb"))
