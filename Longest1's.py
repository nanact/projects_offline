def longest_consecutive_ones(n):
    binary = bin(n)[2:]
    return max(len(seq) for seq in binary.split('0'))

n = 222
print("Longest consecutive 1's:", longest_consecutive_ones(n))