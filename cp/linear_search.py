def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

num_elements = int(input("Enter the number of elements in the array: "))
array = [int(input(f"Enter element {i + 1}: ")) for i in range(num_elements)]
target = int(input("Enter the element to search: "))
index = linear_search(array, target)

if index != -1:
    print(f"Element {target} found at index {index}")
else:
    print(f"Element {target} not found.")
