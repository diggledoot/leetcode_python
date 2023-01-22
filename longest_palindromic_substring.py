def find_longest_palindrome(s):
    longest = ''
    n = len(s)

    if n == 1:
        return s

    if n == 2:
        if s == s[::-1]:
            return s

    for i in range(n):
        for j in range(i+1,n+1): #n+1 here because we want to till the end at 13
            word = s[i:j]
            if word == word[::-1]:
                if len(word)>len(longest):
                    longest = word
    return longest


print(find_longest_palindrome('locoannamadam'))
# madam

print(find_longest_palindrome("bb"))
