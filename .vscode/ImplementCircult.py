def solve_circuit(a, b, c):
    return (a and not b) or (b and c)

a = 1
b = 0
c = 1
print("Circuit output:", solve_circuit(a, b, c))