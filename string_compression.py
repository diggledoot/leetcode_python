chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
count = 1
for i in range(len(chars) - 1, -1, -1):
    if i and chars[i] == chars[i - 1]:
        count += 1
        chars.pop(i)
    else:
        if count > 1:
            for item in str(count)[::-1]:
                chars.insert(i + 1, item)
            count = 1
print(count)


# compressed = ""
# curr_char = s[0]
# count = 1

# for i in range(1, len(s)):
#     if s[i] == curr_char:
#         count += 1
#     else:
#         compressed += curr_char + ("" if str(count) == "1" else str(count))
#         count = 1
#         curr_char = s[i]
# compressed += curr_char + ("" if str(count) == "1" else str(count))

# print(list(compressed))
