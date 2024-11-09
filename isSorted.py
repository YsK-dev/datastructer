def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True

my_list = [10, 20, 30, 40]
print(is_sorted(my_list))  # Output: True
