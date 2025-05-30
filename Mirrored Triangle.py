
size = int(input("Enter the size of the triangle: "))

for i in range(1, size + 1):
    print(" " * (size - i) + "*" * i)