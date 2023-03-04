def generate_numbers_generator(max):
    for num in range(1, max + 1):
        yield num


def generate_numbers_list(max):
    numbers = [num for num in range(1, max + 1)]
    return numbers


# Using a generator
for num in generate_numbers_generator(5):
    print(num)

# Using a lists
for num in generate_numbers_list(5):
    print(num)

"""
Generator expressions
"""
# Example 1: Generate the squares of numbers from 1 to 10
squares = (x**2 for x in range(1, 11))
for square in squares:
    print(square)

# Example 2: Generate the even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = (x for x in numbers if x % 2 == 0)
for even in evens:
    print(even)
"""
Generator expressions are a concise and memory-efficient way to create generators, similar to list comprehensions but with round parentheses () instead of square brackets []. They can be useful when working with large data sets or when memory is a concern.
"""
