from functools import reduce

num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

size = int(input("Enter the size of the triangle: "))
for i in range(1, size + 1):
    print(" " * (size - i) + "*" * i)

bill_amount = float(input("Enter the total bill amount: "))
amount_paid = float(input("Enter the amount paid: "))
due_amount = bill_amount - amount_paid
if due_amount > 0:
    print(f"The customer still owes {due_amount:.2f}.")
elif due_amount < 0:
    print(f"Change to return: {-due_amount:.2f}.")
else:
    print("The bill is fully paid. No amount due.")

numbers = (2, 3, 5, 7, 11)
product = reduce(lambda x, y: x * y, numbers)
print(f"The product of the numbers in the tuple is: {product}")

test_dict = {'a': 2, 'b': 3, 'c': 2, 'd': 4, 'e': 2}
value = int(input("Enter the value to check frequency: "))
frequency = list(test_dict.values()).count(value)
print(f"The frequency of {value} in the dictionary is: {frequency}")

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
symmetric_diff = set1 ^ set2
print(f"The symmetric difference between the sets is: {symmetric_diff}")

squares = [x**2 for x in range(1, 11)]
print(f"Squares from 1 to 10: {squares}")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print(f"Even numbers: {evens}")

words = ["apple", "banana", "cherry", "date"]
lengths = [len(word) for word in words]
print(f"Lengths of words: {lengths}")

fruits = ["apple", "banana", "cherry"]
upper_fruits = [fruit.upper() for fruit in fruits]
print(f"Uppercase fruits: {upper_fruits}")