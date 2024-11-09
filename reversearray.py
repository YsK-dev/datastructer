def reverse_array(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        print("this is start: ",start)
        start += 1
        end -= 1
        print("this is end: ",end)
    return arr

my_list = [1, 2, 3, 4, 5]
print(reverse_array(my_list))  # Output: [5, 4, 3, 2, 1]
