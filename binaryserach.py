def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
            print("thıh ıs low ",low)
        else:
            high = mid - 1
            print("this is high ",high)

        
    return -1

target=47
binary_search([1,2,4,89,90,45,67,75,867,98756,35,47],target)

print("thıs ıs target",target)