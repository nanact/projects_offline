from functools import reduce

numbers = (2, 3, 5, 7, 11)

product = reduce(lambda x, y: x * y, numbers)

print(f"The product of the numbers in the tuple is: {product}")