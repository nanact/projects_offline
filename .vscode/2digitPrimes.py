def two_digit_primes():
    primes = []
    for num in range(10, 100):
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)
    return primes

print("Two-digit prime numbers:", two_digit_primes())