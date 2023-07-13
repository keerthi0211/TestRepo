def SelectionSort(arr):
    n=len(arr)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = input("Enter a list of (space-separated): ").split()
arr = [int(num) for num in arr]
sorted_arr=SelectionSort(arr)
print("sorted array is :", sorted_arr)
