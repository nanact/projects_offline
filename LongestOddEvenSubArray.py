def longest_alternating_subarray(arr):
    if not arr:
        return 0

    max_len = curr_len = 1

    for i in range(1, len(arr)):
        if (arr[i] % 2 == 0 and arr[i-1] % 2 != 0) or (arr[i] % 2 != 0 and arr[i-1] % 2 == 0):
            curr_len += 1
            max_len = max(max_len, curr_len)
        else:
            curr_len = 1

    return max_len

arr = [1, 3, 5, 4, 7, 10, 11, 13]
print("Longest alternating odd-even subarray length:", longest_alternating_subarray(arr))