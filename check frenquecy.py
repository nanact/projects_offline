test_dict = {'a': 2, 'b': 3, 'c': 2, 'd': 4, 'e': 2}

value = int(input("Enter the value to check frequency: "))

frequency = list(test_dict.values()).count(value)

print(f"The frequency of {value} in the dictionary is: {frequency}")