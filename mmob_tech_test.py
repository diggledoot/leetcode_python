myList = [
    25,
    "apple",
    ["banana", "strawberry", "apple", ["mango", 13, "apple", "strawberry"], 25],
]


def numberOfItems(theList, item):
    itemType = type(item)
    count = 0

    for i in theList:
        if itemType == int and i == item:
            count += 1
        elif itemType == str and i == item:
            count += 1
        elif type(i) == list:
            count += numberOfItems(i, item)
    return count


print(numberOfItems(myList, "apple"))

# within a week~~
