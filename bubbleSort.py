def BubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = input("Enter a list of numbers (space-separated): ").split()
arr = [int(num) for num in arr]
sorted_arr=BubbleSort(arr)
print("sorted array is :", sorted_arr)