def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def decimal_to_binary(n):
    return bin(n)[2:]

def list_length(lst):
    count = 0
    for _ in lst:
        count += 1
    return count

def all_substrings(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])
    return substrings

def linear(n):
    if n == 0:
        return 0
    return n + linear(n - 1)

def tree(n):
    if n <= 1:
        return 1
    return tree(n - 1) + tree(n - 2)

def divide(n):
    if n <= 1:
        return
    divide(n // 2)
    divide(n // 2)

def print_recurrence_relations():
    print("Recurrence Relations:")
    print("1. Linear Recursion       → T(n) = T(n - 1) + c        → O(n)")
    print("2. Tree Recursion         → T(n) = T(n - 1) + T(n - 2) + c → O(2ⁿ)")
    print("3. Divide & Conquer       → T(n) = 2T(n / 2) + c        → O(n)")

def rightmost_set_bit(n):
    return n & -n

def solve_circuit(a, b, c):
    return (a and not b) or (b and c)

def two_digit_primes():
    primes = []
    for num in range(10, 100):
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)
    return primes

def find_lcm(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return abs(a * b) // gcd(a, b)

n = 5
lst = [10, 20, 30, 40, 50]
s = "cat"
a = 1
b = 0
c = 1

print("Binary to Decimal:", binary_to_decimal("1101"))
print("Decimal to Binary:", decimal_to_binary(13))
print("List Length:", list_length(lst))
print("All Substrings:", all_substrings(s))
print("Linear Recursion Output:", linear(n))
print("Tree Recursion Output:", tree(n))
divide(n)
print_recurrence_relations()
print("Rightmost Set Bit:", rightmost_set_bit(18))
print("Circuit Output:", solve_circuit(a, b, c))
print("Two-Digit Primes:", two_digit_primes())
print("LCM:", find_lcm(12, 18))