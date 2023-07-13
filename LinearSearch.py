def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = input("Enter a list of numbers (space-separated): ").split()
arr = [int(num) for num in arr]
target = int(input("Enter the target number: "))

result = linear_search(arr, target)
if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")