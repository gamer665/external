num_elements = int(input("Enter the number of elements in the array: "))
array = []
for i in range(num_elements):
    value = float(input(f"Enter element {i + 1}: "))
    array.append(value)
total_sum = 0
for value in array:
    total_sum += value
print(f"The sum of the array values is: {total_sum}")
