num_elements = int(input("Enter the number of elements in the array: "))
array = []
for i in range(num_elements):
    value = float(input(f"Enter element {i + 1}: "))
    array.append(value)

# Manual sorting using Bubble Sort
for i in range(len(array)):
    for j in range(0, len(array) - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print("Sorted array:", array)
