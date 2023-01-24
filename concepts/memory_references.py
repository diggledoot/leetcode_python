x = 5
y = x
print(x)  # prints 5
print(y)  # prints 5

x = 6
print(x)  # prints 6
print(y)  # prints 5
"""
In this example, we first create a variable x and assign it the value of 5. Then we create a second variable y and assign it the value of x. Both x and y are now references to the same memory location where the value 5 is stored. When we change the value of x to 6, the value stored in the memory location is also updated, but y still references the original memory location, so it still has the value 5.
"""

a = [1, 2, 3]
b = a
print(a)  # prints [1, 2, 3]
print(b)  # prints [1, 2, 3]

a.append(4)
print(a)  # prints [1, 2, 3, 4]
print(b)  # prints [1, 2, 3, 4]

"""
In this example, we first create a list a and assign it the values [1, 2, 3]. Then we create a second variable b and assign it the value of a. Now, a and b are references to the same list object in memory. When we append an element to the list using a, it modifies the same object in memory, so the change is also visible through the b reference.
"""

x = 5
y = x
print(id(x))  # prints the memory address of x
print(id(y))  # prints the memory address of y, which is the same as x

x = x + 1
print(x)  # prints 6
print(y)  # prints 5
print(id(x))  # prints a different memory address than before
print(id(y))  # prints the same memory address as before

"""
In this example, we first create a variable x and assign it the value of 5. Then we create a second variable y and assign it the value of x. Both x and y are now references to the same memory location where the value 5 is stored. When we add 1 to x, it creates a new memory address to store the new value 6, so it is different from the memory address of y, which still holds the value 5.
"""
