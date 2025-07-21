def linear_recursion(n):
    if n == 0:
        return 0
    return n + linear_recursion(n - 1)

def tree_recursion(n):
    if n <= 1:
        return 1
    return tree_recursion(n - 1) + tree_recursion(n - 2)

n = 5
print("Linear Recursion (Sum to n):", linear_recursion(n))
print("Tree Recursion (Fibonacci):", tree_recursion(n))