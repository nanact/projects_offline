def countdown(n):
    if n == 0:
        return "Done"
    print(f"Counting down: {n}")
    return countdown(n - 1)