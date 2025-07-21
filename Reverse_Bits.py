def reverse_bits(n):
    binary = bin(n)[2:]
    reversed_binary = binary[::-1]
    return int(reversed_binary, 2)

n = 13
print("Reversed bit number:", reverse_bits(n))