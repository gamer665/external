def bubble_sort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

num_elements = int(input("Enter the number of elements in the array: "))
array = [float(input(f"Enter element {i + 1}: ")) for i in range(num_elements)]
sorted_array = bubble_sort(array)
print("Sorted array using Bubble Sort:", sorted_array)
