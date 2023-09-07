def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Take user input for the list of numbers
input_str = input("Enter a list of numbers separated by spaces: ")
arr = [int(num) for num in input_str.split()]

print("Before sorting:", arr)
arr = bubble_sort(arr)
print("After sorting:", arr)

'''
Enter a list of numbers separated by spaces: 22 99 56 23 51 7 10 69
Before sorting: [22, 99, 56, 23, 51, 7, 10, 69]
After sorting: [7, 10, 22, 23, 51, 56, 69, 99]'''