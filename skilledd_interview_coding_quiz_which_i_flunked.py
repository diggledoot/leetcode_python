# Problem Statement:
# In this coding test, we will be given a list of products and their prices at different times.
# Your task is to implement a function that takes in this list and returns the lowest price of each product at each time.

# Input:
# A list of int tuples representing the products and their prices at different times in the form (product_name, timestamp, price)
# Example: prices = [("Shampoo", 2, 4), ("Shampoo", 1, 5), ("Shampoo", 2, 6), ("Toothpaste", 1, 3), ("Toothpaste", 1, 2)]

# Explanation: ("Shampoo", 2, 6) is removed because there is a Shampoo at timestamp 2 that is cheaper
# For the same reason, ("Toothpaste", 1, 3) is removed

# Assumptions:
# - The input list is not guaranteed to be ordered in any way
# - The same product can have multiple prices at the same timestamp

# My solution
def lowest_price(prices):
    result = {}

    for product, time, price in prices:
        if product not in result:
            result[product] = []
        result[product].append([time, price])

    for product in result:
        temp = result[product]
        time = None
        price = None
        for key, value in temp:
            if price == None:
                time = key
                price = value
                continue
            if price > value:
                time = key
                price = value
        result[product].clear()
        result[product].append([time, price])

    return result


# ChatGPT's solution, elegant af
def chatgpt_lowest_price(data):
    prices = {}
    for item in data:
        product, timestamp, price = item
        if product not in prices or prices[product][1] > price:
            prices[product] = (timestamp, price)
    return prices


prices = [
    ("Shampoo", 2, 4),  # should appear
    ("Shampoo", 1, 5),
    ("Shampoo", 2, 6),
    ("Toothpaste", 1, 3),
    ("Toothpaste", 1, 2),  # should appear
]
print("product:[time,price]")
print(chatgpt_lowest_price(prices))
