def binary_search(array, target):
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

num_elements = int(input("Enter the number of elements in the array: "))
array = [int(input(f"Enter element {i + 1}: ")) for i in range(num_elements)]
array.sort()  # Binary Search requires a sorted array
print("Sorted array for Binary Search:", array)
target = int(input("Enter the element to search: "))
index = binary_search(array, target)

if index != -1:
    print(f"Element {target} found at index {index}")
else:
    print(f"Element {target} not found.")
