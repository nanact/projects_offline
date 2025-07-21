def rightmost_set_bit(n):
    return n & -n

n = 18
print("Rightmost set bit of", n, "is:", rightmost_set_bit(n))