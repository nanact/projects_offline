def is_power_of_8(n):
    if n <= 0:
        return False
    while n % 8 == 0:
        n //= 8
    return n == 1
number = int(input("Enter a number: "))
if is_power_of_8(number):
    print(f"{number} is a power of 8.")
else:
    print(f"{number} is not a power of 8.")