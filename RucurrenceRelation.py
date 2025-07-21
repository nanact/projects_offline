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

n = 5
print("Linear Recursion Output (Sum to n):", linear(n))
print("Tree Recursion Output (Fibonacci of n):", tree(n))
divide(n)
print_recurrence_relations()