def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

my_list = [10, 20, 5, 30, 25]
print(find_max(my_list))  # Output: 30
