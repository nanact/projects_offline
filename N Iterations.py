def multiply_single_iteration(N, M):
    return N * M

def multiply_n_iterations(N, M):
    result = 0
    for _ in range(N):
        result += M
    return result

# Example usage:
N = 5
M = 3

print("Single Iteration:", multiply_single_iteration(N, M))
print("N Iterations:", multiply_n_iterations(N, M))