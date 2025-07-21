def find_lcm(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return abs(a * b) // gcd(a, b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("LCM:", find_lcm(a, b))