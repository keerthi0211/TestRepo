def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def MergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = MergeSort(left)
    right = MergeSort(right)
    return merge(left, right)

arr = input("Enter a list of numbers (space-separated): ").split()
arr = [int(num) for num in arr]
sorted_arr=MergeSort(arr)
print("sorted array is :", sorted_arr)