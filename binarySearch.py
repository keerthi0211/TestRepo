def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

arr = input("Enter a sorted list of numbers (space-separated): ").split()
arr = [int(num) for num in arr]
target = int(input("Enter the target number: "))

result = binary_search(arr, target)
if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")