def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

num_elements = int(input("Enter the number of elements in the array: "))
array = [float(input(f"Enter element {i + 1}: ")) for i in range(num_elements)]
sorted_array = insertion_sort(array)
print("Sorted array using Insertion Sort:", sorted_array)
