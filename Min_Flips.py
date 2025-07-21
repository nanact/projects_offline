def min_flips(arr):
    if not arr:
        return 0

    flips_to_0 = flips_to_1 = 0
    prev = arr[0]

    for current in arr[1:]:
        if current != prev:
            if current == 1:
                flips_to_0 += 1
            else:
                flips_to_1 += 1
        prev = current

    if arr[0] == 0:
        flips_to_1 += 1
    else:
        flips_to_0 += 1

    return min(flips_to_0, flips_to_1)

arr = [1, 0, 0, 1, 0, 1, 1]
print("Minimum flips needed:", min_flips(arr))