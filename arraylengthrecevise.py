def list_length(lst):
    count = 0
    for _ in lst:
        count += 1
    return count

lst = [10, 20, 30, 40, 50]
print("Length of the list:", list_length(lst))